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