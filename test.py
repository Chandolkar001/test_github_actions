import json
import hmac
import base64
import urllib3
import hashlib
from urllib3.util.retry import Retry
import requests
from requests.adapters import HTTPAdapter

def retry_session(retries, session=None, backoff_factor=0.3):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def upload_response(findings):
    url = "https://d58f-106-201-240-125.ngrok-free.app"
    token = "asdf1234"

    headers = {
        "content-type": "application/json",
        "Authorization": f"Bearer {token}",

    }
    data = {
        "organization": {
            "login": "asd",
        },
        "repository": {
            "full_name": "asd",
            "branch": "asd",
            "commits": "asd",
        },
        "event": "asd",
        "commits": "asd",
        "pr": "asd",
        "findings": findings,
        "sender": {
            "login": "asd",
        },
    }

    digest = hmac.new(token.encode("utf-8"), json.dumps(data, separators=(",", ":")).encode("utf-8"), hashlib.sha256)
    signedValue = "sha256=" + digest.hexdigest()
    headers["hmac"] = signedValue

    final_report = base64.b64encode(json.dumps(data).encode("utf-8")).decode("utf-8")

    data = {
        "data": final_report,
    }

    try:
        # session = retry_session(retries=5)
        # session.post(url="https://d58f-106-201-240-125.ngrok-free.app", data=json.dumps(data))
        retries = urllib3.Retry(3, status_forcelist=[502, 503, 504], backoff_factor=10)
        http = urllib3.PoolManager(retries=retries)
        response = http.request("POST", url=url, json=data, headers=headers)
        print(f"report submitted, {response.status}")
    except urllib3.exceptions.LocationValueError as e:
        print(f"connection failed: {e}")
        raise urllib3.exceptions.MaxRetryError("Retry limit reached") from e
fin = dict()
fin["msg"] = "hello"
upload_response(findings=fin)


