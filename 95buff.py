import os
import requests

# 从环境变量获取组合后的账号和密码
login_credentials = os.getenv("LOGIN_CREDENTIALS")

# 分割账号和密码
account, password = login_credentials.split(":")

url = "https://95buff.com/api/login/doLogin"

headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json;charset=UTF-8",
    "devicetype": "pc",
    "origin": "https://95buff.com",
    "referer": "https://95buff.com/",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

data = {
    "account": account,  # 从 Secret 中解析出的账号
    "password": password,  # 从 Secret 中解析出的密码
    "isMobile": "1",
    "device": "pc"
}

response = requests.post(url, headers=headers, json=data)

print(f"Response status code: {response.status_code}")
print(f"Response text: {response.text}")
