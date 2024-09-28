import os
import requests

# 从环境变量获取多个账号登录凭据
login_credentials = os.getenv("BUFF95")
if not login_credentials:
    print("请设置环境变量 BUFF95，格式为 '账号:密码;账号2:密码2'")
    exit(1)

# 分割多个账号和密码，假设每个账号用';'分隔
accounts = login_credentials.split(';')

# 登录 URL 和 Headers
login_url = "https://95buff.com/api/login/doLogin"
headers = {
    "accept": "application/json, text/plain, */*",
    "content-type": "application/json;charset=UTF-8",
    "devicetype": "pc",
    "origin": "https://95buff.com",
    "referer": "https://95buff.com/",
    "sec-ch-ua-platform": '"Windows"',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0"
}

# 遍历每个账号进行登录和开箱操作
for account_info in accounts:
    try:
        # 分割账号和密码
        account, password = account_info.split(':')
    except ValueError:
        print(f"账号信息格式错误：{account_info}，应该是 '账号:密码'")
        continue

    # 登录请求数据
    data = {
        "account": account,
        "password": password,
        "isMobile": "1",
        "device": "pc"
    }

    # 发送登录请求
    response = requests.post(login_url, headers=headers, json=data)

    # 检查登录响应状态
    if response.status_code == 200:
        # 获取 token
        token = response.json().get("data", {}).get("data", {}).get("token")
        print(f"账号 {account} 登录成功，Token: {token}")

        # 如果成功获取 token，进行开箱操作
        if token:
            open_box_url = "https://95buff.com/api/gradeBox/openBox"
            headers['authorization'] = token  # 替换为新的authorization头

            # 请求体，设置id为483
            open_box_data = {
                "id": 483
            }

            response_open_box = requests.post(open_box_url, headers=headers, json=open_box_data)

            # 打印打开箱子的响应
            print(f"账号 {account} 开箱结果：{response_open_box.text}")
        else:
            print(f"账号 {account} 无法获取token")
    else:
        print(f"账号 {account} 登录失败，无法获取token")
