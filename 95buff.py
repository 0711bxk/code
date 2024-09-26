import os
import requests

# 从环境变量获取组合后的账号和密码
login_credentials = os.getenv("BUFF95")

if login_credentials is None:
    print("Error: BUFF95 environment variable is not set.")
    exit(1)  # 退出脚本

# 分割账号和密码
try:
    account, password = login_credentials.split(":")
except ValueError:
    print("Error: BUFF95 format is incorrect. Expected 'account:password'.")
    exit(1)

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

# 从响应中提取token
if response.status_code == 200:
    token = response.json().get("data", {}).get("data", {}).get("token")

    # 使用token进行第二个请求
    if token:
        open_box_url = "https://95buff.com/api/gradeBox/openBox"
        headers['authorization'] = token  # 替换为新的authorization头

        # 请求体
        open_box_data = {
            "id": 483  # 设置id为483
        }

        response_open_box = requests.post(open_box_url, headers=headers, json=open_box_data)
        print(response_open_box.text)
    else:
        print("无法获取token")
else:
    print("登录失败，无法获取token")

