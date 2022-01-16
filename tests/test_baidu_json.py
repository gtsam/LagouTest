# coding=utf-8
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


# ddt一定是装饰在TestCase的子类上
@ddt
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    # 此处测试数据从文件读取，使用@file_data装饰器
    # 文件路径是相对于Baidu这个测试类的相对路径
    # 使用外部文件方式Load数据无须使用unpack
    @file_data('test_baidu.json')
    def test_baidu_search(self, search_string, expect_string):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element(By.ID, "kw").send_keys(search_string)
        driver.find_element(By.ID, "su").click()

        time.sleep(2)

        # 获取元素内的全部HTML
        search_results = driver.find_element(By.XPATH, '//*[@id="1"]/h3/a').get_attribute('innerHTML')
        print('全部HTML：', search_results)
        self.assertEqual(expect_string in search_results, True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)
