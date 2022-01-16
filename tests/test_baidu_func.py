# coding=utf-8
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time


def get_test_data():
    # 这里写你获取测试数据的业务逻辑。
    # 获取到后，把数据返回即可。
    # 注意，如果多组数据，需要返回类似([数据1-参数1， 数据1-参数2]，[数据2-参数1， 数据2-参数2])这样的格式，方便ddt.data()解析
    results = ['iTesting', 'iTesting'], ['helloqa.com', 'iTesting']
    return results


# ddt一定是装饰在TestCase的子类上
@ddt
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    # data表示data是直接提供的。注意data里的参数我写了函数get_test_data()的返回值，并且以*为前缀，代表返回的是可变参数。
    # unpack表示，对于每一组数据，如果它的值是list或者tuple，那么就分拆成独立的参数
    @data(*get_test_data())
    @unpack
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
