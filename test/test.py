import requests
import pandas as pd
import json
import time
import datetime
def main():
    url = "http://35.194.189.215:8000/insert"
    
    data = {"name":"GG","age":int(time.time()),"address":datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"salary":int(time.time())}
    payload = json.dumps(data).encode("utf-8")
    headers = {
    'Content-Type': 'application/json'
    }
    r = requests.request("POST", url, headers=headers, data=payload)
    print(r.text)



if __name__ == "__main__":
    main()