import requests

if __name__ == '__main__':
    # 发送get请求 --带参数
    # 等同于直接访问https://httpbin.org/get?kevin=hello
    requests.get('https://httpbin.org/get', params={'kevin': 'hello'})

    # 当访问接口发生301跳转时，可以设置允许或者禁止跳转
    requests.get('http://github.com/', allow_redirects=False)

    # 发送get请求， 加proxy
    proxies = {'http': 'http://10.10.1.10:3128',
               'https': 'http://10.10.1.10:1080'}
    requests.get('https://httpbin.org/get', proxies=proxies)

    # 发送get请求，加鉴权 -- Basic Auth
    # 首先导入HTTPBasicAuth，一般导入语句写在py文件的最前面。
    from requests.auth import HTTPBasicAuth
    requests.get('https://api.github.com/user', auth=HTTPBasicAuth('user', 'password'))

    # 发送get请求，加鉴权 -- Digest Auth
    # 首先导入HTTPDigestAuth，一般导入语句写在py文件的最前面。
    from requests.auth import HTTPDigestAuth
    requests.get('https://api.github.com/user', auth=HTTPDigestAuth('user', 'password'))

    # OAuth 1 Authentication
    # 首先安装requests_oauthlib （可通过pip install）
    from requests_oauthlib import OAuth1
    url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
    auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
    requests.get(url, auth=auth)

    url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
    cookie = {'cookie': 'edu_gate_login_token=$$$EDU_eyJraWQiOiIyZDBhODJmMi05ZDk1LTQ5MWItYmNiMC03ZjRmZWIxOWM4ZTMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0Z3QiOiJfQ0FTX1RHVF9UR1QtMDdmNmU3NTlmNTQzNDc4MWEyM2UxMjM4ZmI2OWVjYzgtMjAyMTA4MDExNDA1NTItX0NBU19UR1RfIiwic3ViIjoiMTk3NzQ1MjEiLCJpcCI6IjIyMi42OS4xNTUuNDAiLCJpc3MiOiJlZHUubGFnb3UuY29tIiwidG9rZW5UeXBlIjoxLCJleHAiOjE2Mjg0MDI3NTIsImlhdCI6MTYyNzc5Nzk1Mn0.Xk2RvFNEm1Q89rfa0U_ivIylTh7Kg72UjR3qg7xStH38J4e1uIize3zL7MkkuWfmDw618Za2IFjnyS1663qNoEvtBV62cMw--rQ6Dw_gEStvfq2ppMLCkEL6jIiVA89RgRoTy6-LT9q8ngJIZXvlGGsnVqo_4lNo9LmIHICpuRzDvGXOcTrCPVZhN-VGmZ65idbpNUtNRIYUR3wxUn9Ss6g7_qs3zSekzVrGmW0FTyv0hP1hs_3IavjY_sYe5R2mKduR1hZbX0lbNzMbgPVIGzgok6gRMG7OxdHW3bu64rjVqLRUhnSnWRn6jRG1bUekdXL2Z1Dez3re8d8ytJcrTA; gate_login_token=675d15a5a57e055e52ba092c6403b440232674b85e5ffb7e38f46ee293da7412;'}
    headers = {'x-l-req-header': '{deviceType: 9}'}
    s = requests.Session()
    # 直接带登录态发送请求
    r = s.get(url, cookies=cookie, headers=headers)
    # 不经过登录，也能访问登录后才能访问的接口
    print(r.text)