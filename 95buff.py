import requests

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
    "account": "18671189740",
    "password": "123456789bxk",
    "isMobile": "1",
    "device": "pc"
}
response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.text)
