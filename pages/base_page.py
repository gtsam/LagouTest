# -*- coding: utf-8 -*-
import json
import traceback
import requests
from selenium import webdriver
from page_objects import PageObject, PageElement
from ..common.requests_helper import SharedAPI  # 需要写相对路径，不然pytest执行的时候找不到对应的目录
from ..common.selenium_helper import SeleniumHelper  # 需要写相对路径，不然pytest执行的时候找不到对应的目录

class BasePage(PageObject):

    def __init__(self, login_credential, target_page):
        self.api_driver = SharedAPI()
        self.loginResult = self.api_driver.login(login_credential)
        self.driver = SeleniumHelper.initial_driver()
        self._api_login(login_credential, target_page)

    def _api_login(self, login_credential, target_page):
        target_url = json.loads(json.dumps(target_page))
        assert json.loads(self.loginResult.text)["user"]["email"].lower() == login_credential["email"]
        all_cookies = self.loginResult.cookies._cookies[".ones.ai"]["/"]
        self.driver.get(target_url["target_page"])
        self.driver.delete_all_cookies()
        for k, v in all_cookies.items():
            self.driver.add_cookie(SeleniumHelper.cookie_to_selenium_format(v))
        self.driver.get(target_url["target_page"])

        return self.driver