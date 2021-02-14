import requests
import pandas as pd
import json
import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import json
import sqlite3
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException


def init_browser(chrome_path=None):
    chrome_options = Options() 
    chrome_options.add_argument('--headless')  #規避google bug
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-default-apps")
    chrome_options.add_argument("--disable-dev-shm-usage")
    if chrome_path is None:
        browser = webdriver.Chrome(ChromeDriverManager().install(),options=chrome_options)
    else:
        browser = webdriver.Chrome(chrome_path,options=chrome_options)        
    return browser


def main():
    browser = init_browser()
    browser.get('http://www.google.com.tw')
    title = browser.title
    print(browser.title)
    browser.close()  

    url = "http://35.194.189.215:8000/insert" 
    ct = datetime.datetime.now()
    data = {"name":title,"age":int(time.time()),"address":ct.strftime("%Y-%m-%d %H:%M:%S"),"salary":int(time.time())}
    payload = json.dumps(data).encode("utf-8")
    headers = {
    'Content-Type': 'application/json'
    }
    r = requests.request("POST", url, headers=headers, data=payload)
    print(r.text)
    with open(f'./data/{ct.strftime("%Y%m%d%H%M%S")}.txt','w+') as f:
        f.write(json.dumps(data))
    print('輸出成功')

    
    



if __name__ == "__main__":
    main()