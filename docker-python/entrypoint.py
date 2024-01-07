import sys
from app import HelloWorld
import subprocess
import os
import json

def get_file_mapping():
    root_dir = "."
    file_map = dict()

    for dir_, _, files in os.walk(root_dir):
        for file_name in files:
            path = os.path.join(dir_, file_name)
            mapping_path = os.path.relpath(path, root_dir)
            file_map[path] = mapping_path
    return file_map

if __name__ == '__main__':
    
    # result = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE)
    # print(result.stdout.decode())
    # print(get_file_mapping())


    # if sys.argv:
    #     hw = HelloWorld(sys.argv[1])
    #     print(hw.greet(12))
    file_exclusions = []
    hash_exclusions = []
    regex_exclusions = []
    custom_regexes = [] 

    if sys.argv[1] != '0':
        file_exclusions = list(sys.argv[1].split(','))
    if sys.argv[2] != '0':
        hash_exclusions = list(sys.argv[2].split(','))
    if sys.argv[3] != '0':
        regex_exclusions = list(sys.argv[3].split())
    if sys.argv[4] != '0':
        custom_regexes = list(sys.argv[4].split())  

    with open('config.json', 'w+') as f:
        json.dump({
            'exclusions': {
                'file': file_exclusions,
                'hash': hash_exclusions,
                'regex': regex_exclusions,
            },
            'custom-regex': custom_regexes
        }, f)

    