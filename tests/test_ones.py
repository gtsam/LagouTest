# -*- coding: utf-8 -*-
import json
import requests
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# 把获取的cookie转换成Selenium/WebDriver能识别的格式
def cookie_to_selenium_format(cookie):
    cookie_selenium_mapping = {'path': '', 'secure': '', 'name': '', 'value': '', 'expires': ''}
    cookie_dict = {}
    if getattr(cookie, 'domain_initial_dot'):
        cookie_dict['domain'] = '.' + getattr(cookie, 'domain')
    else:
        cookie_dict['domain'] = getattr(cookie, 'domain')
    for k in list(cookie_selenium_mapping.keys()):
        key = k
        value = getattr(cookie, k)
        cookie_dict[key] = value
    return cookie_dict

class TestOneAI:
    # 在pytest里，针对一个类方法的setup为setup_method,
    # setup_method作用同unittest里的setUp()
    def setup_method(self, method):
        self.s = requests.Session()
        self.login_url = 'https://ones.ai/project/api/project/auth/login'
        self.home_page = 'https://ones.ai/project/#/home/project'
        self.header = {
            "user-agent": "user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
            "content-type": "application/json"}
        self.driver = webdriver.Chrome()
    # 使用了pytest里的参数化
    @pytest.mark.parametrize('login_data, project_name', [({"password": "Dean_3170833073", "email": "923210866@qq.com"}, {"project_name":"VIPTEST"})])
    def test_merge_api_ui(self, login_data, project_name):
        # 接口登录
        result = self.s.post(self.login_url, data=json.dumps(login_data), headers=self.header)
        # 断言登录成功
        assert result.status_code == 200
        assert json.loads(result.text)["user"]["email"].lower() == login_data["email"]
        # 根据实际情况解析cookies，此处需结合业务场景
        print('session session', self.s.cookies._cookies)
        all_cookies = self.s.cookies._cookies[".ones.ai"]["/"]

        # 删除所有cookies
        self.driver.get(self.home_page)
        self.driver.delete_all_cookies()

        # 把接口登录后的cookie塞到Selenium driver里去，传递登录状态
        for k, v in all_cookies.items():
            self.driver.add_cookie(cookie_to_selenium_format(v))

        # 再次访问目标页面，此时登录状态已经传递过来了
        self.driver.get(self.home_page)

        # 查找项目元素，获取元素的值，并进行断言
        # 注意，此时我浏览器操作就不需再登录了
        try:
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '[class="text-overflow-hidden company-title-text"]')))

            time.sleep(3)

            # 断言我的项目存在
            assert element.get_attribute("innerHTML") == project_name["project_name"]
        except TimeoutError:
            raise TimeoutError('Run time out')
    # 在pytest里，针对一个类方法的teardown为teardown_method,
    # teardown_method作用同unittest里的dearDown()
    def teardown_method(self, method):
        self.s.close()
        self.driver.quit()

if __name__ == '__main__':
    one_ai = TestOneAI()
    one_ai.test_merge_api_ui()