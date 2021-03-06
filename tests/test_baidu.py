# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import pytest
import time


@pytest.mark.baidu
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    @pytest.mark.BaiduSearch
    def test_baidu_search(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element(By.ID, "kw").send_keys("iTesting")
        driver.find_element(By.ID, "su").click()

        time.sleep(2)

        # 获取元素内的全部HTML
        search_results = driver.find_element(By.XPATH, '//*[@id="1"]/h3/a').get_attribute('innerHTML')
        print('全部HTML：', search_results)
        self.assertEqual('iTesting' in search_results, True)

    @unittest.skip('i want to skip')
    def test_baidu_set(self):
        driver = self.driver
        driver.get(self.base_url + "/gaoji/preferences.html")
        m = driver.find_element(By.XPATH, ".//*[@id='nr']")
        m.find_element_by_xpath("//option[@value='10']").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
