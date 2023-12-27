import sys
import os
import json
import requests
from tabulate import tabulate
from detect_secrets import SecretsCollection
from detect_secrets.settings import transient_settings
from detect_secrets.settings import default_settings, get_settings
from typing import List, Any

class Validation:
    def __init__(self, headers: dict = None, url: str = None, method: str = "get"):
        self.headers = headers
        self.url = url
        self.method = method

    def parse_headers(self, secret):
        for key in self.headers:
            self.headers[key] = self.headers[key].replace("{secret}", secret)

    def validate(self, secret):
        self.parse_headers(secret)
        if self.method.lower() == "post":
            response = requests.post(url=self.url, headers=self.headers)
        else:
            response = requests.get(url=self.url, headers=self.headers)
        if response.status_code == 200:
            return True
        return False


def get_file_mapping():
    root_dir = "actions"
    file_map = dict()

    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            path = os.path.join(dir_, file_name)
            mapping_path = os.path.relpath(path, root_dir)
            file_map[path] = mapping_path
    return file_map


def get_config():
    plugins_used = []
    regexes = []
    with default_settings():
        plugins = list(get_settings().plugins.keys())
        for plugin in plugins:
            plugins_used.append({'name': plugin})

    with open('default_regexes.json', 'r') as file:
        default_regex = json.load(file)
    regexes = regexes + default_regex['patterns']

    for i in regexes:
        val = repr(i['regex'])[1:-1]
        i['regex'] = val

    mapping = {}
    with open('validations_mapping.json') as file:
        mapping = json.load(file)
    validations = []

    for name in mapping:
        val = Validation(headers=mapping[name]["headers"], url=mapping[name]["url"], method=mapping[name]["method"])
        pair = {"name": name, "function": val.validate}
        validations.append(pair)
    config = {
        'plugins_used': plugins_used,
        'custom_regex': regexes,
        'verify': validations,
        'filters_used': [
            {"path": "detect_secrets.filters.common.is_ignored_due_to_verification_policies",
             "min_level": 1,
             }
        ]
    }
    return config

def get_commit_sha():
    return os.environ["GITHUB_SHA"]


def get_branch():
    return os.environ["GITHUB_REF_NAME"]

def parse_secrets(secrets: Any) -> list:
    new_secrets = []
    secrets = secrets.json()
    for group in secrets:
        for secret in secrets[group]:
            new_secret = {
                "commitHash": secret['commit'],
                "fileName": secret['filename'],
                "lineNumber": secret['line_number'],
                "regex": secret['type'],
                "hashedValue": secret['hashed_secret'],
                "isHashedValueSkipped": secret['notify'],
                "branch": secret['branch'],
            }
            if secret["is_verified"]:
                new_secret["isVerified"] = True
                new_secret["isValid"] = True
            elif not secret["is_verified"]:
                new_secret["isVerified"] = True
                new_secret["isValid"] = False
            else:
                new_secret["isVerified"] = False
                new_secret["isValid"] = None
            
            new_secrets.append(new_secret)

    return new_secrets

def print_table(secrets):
    display_headers = ["Commit SHA", "File Name", "Line Number", "Plugin", "Is Verified", "Is Valid"]
    table_data = [[entry["commitHash"], entry["fileName"], entry["lineNumber"], entry["regex"], entry["isVerified"], entry["isValid"]] for entry in secrets]
    table = tabulate(table_data, headers=display_headers, tablefmt='grid')
    print(table)

if __name__ == '__main__':
    secret_collection = SecretsCollection()
    config = get_config()
    commit_id = get_commit_sha()
    branch = get_branch()
    file_mapping = get_file_mapping()

    with transient_settings(config=config):
        new_secret = SecretsCollection()
        new_secret.scan_files(*(file_mapping.keys()))
        new_secret.rename_files(filelist=file_mapping)
        new_secret.add_commit(commit_id)
        new_secret.add_branch(branch)
        all_secrets = parse_secrets(new_secret)
        if all_secrets:
            print(f"Branch: {branch}")
            print_table(all_secrets)
        else:
            print("No Secrets Detected")
