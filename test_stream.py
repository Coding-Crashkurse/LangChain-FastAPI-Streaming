import json

import requests

url = "http://localhost:6655/stream_chat"
message = "Hello, how are you?"
data = {"message": message}

headers = {"Content-type": "application/json"}

with requests.post(url, data=json.dumps(data), headers=headers, stream=True) as r:
    for chunk in r.iter_content(1024):
        print(chunk)
