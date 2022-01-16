# coding=utf-8
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


# 使用yaml文件前先尝试导入，导入失败则将skip使用yaml数据驱动的测试用例
try:
    import yaml
except ImportError:
    have_yaml_support = False
else:
    have_yaml_support = True
needs_yaml = unittest.skipUnless(
    have_yaml_support, "Need YAML to run this test"
)


# ddt一定是装饰在TestCase的子类上
@ddt
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    # 使用yaml文件必须使用@needs_yaml装饰
    @needs_yaml
    @file_data('test_baidu.yaml')
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
