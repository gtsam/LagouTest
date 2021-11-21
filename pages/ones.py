# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects import PageObject, PageElement
from ..pages.base_page import BasePage  # 需要写相对路径，不然pytest执行的时候找不到对应的目录

class OneAI(BasePage):
    PROJECT_NAME_LOCATOR = '[class="text-overflow-hidden company-title-text"]'
    NEW_PROJECT_LOCATOR = '.ones-btn.ones-btn-primary'
    new_project = PageElement(css=NEW_PROJECT_LOCATOR)
    def __init__(self, login_credential, target_page):
        super().__init__(login_credential, target_page)
    def get_project_name(self):
        try:
            project_name = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, self.PROJECT_NAME_LOCATOR)))
            return project_name.get_attribute("innerHTML")
        except TimeoutError:
            raise TimeoutError('Run time out')