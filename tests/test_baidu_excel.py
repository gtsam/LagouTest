# coding=utf-8
from ddt import ddt, data, file_data, unpack
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import time
import xlrd


def read_excel(file_name):
    """
    打开excel文件
    :param file_name:
    """
    try:
        book=xlrd.open_workbook(file_name)
        return book
    except Exception as e:
        print('读取excel发生错误{}'.format(e))


def read_excel_by_name(sheet_name,file_name):
    """
    根据excel的sheet的名称读取excel
    :param file_name:
    :param sheet_name:
    """
    try:
        book=read_excel(file_name)
        sheet=book.sheet_by_name(sheet_name)
        data={}
        if sheet is not None:
            rows_data=[]
            nrows=sheet.nrows
            row_values=sheet.row_values
            for row in range(nrows):
                rows_data.append(row_values(row))
            for col_data in rows_data:
                data[col_data[0]]=col_data[1:]
        return  data
    except Exception:
        print('根据名称读取excel发生错误')


def read_excel_by_names(file_name):
    """返回一个字典存放所有的sheet的值{sheet_name:sheet_value}
    :param file_name:
    """
    try:
        book=read_excel(file_name)
        sheet_dict={}
        if book is not None:
            sheet_names=book.sheet_names()
            for sheet_name in sheet_names:
                sheet_dict[sheet_name]=read_excel_by_name(sheet_name, file_name)
        print(sheet_dict)
        return sheet_dict
    except Exception:
        print('循环读取excel各个sheet发生错误!')


def get_test_data(file_name):
    """
    :type file_name: object
    """
    sheet_dict = read_excel_by_names(file_name)
    test1 = sheet_dict['test_baidu']['test1']
    test2 = sheet_dict['test_baidu']['test2']

    return test1, test2


# ddt一定是装饰在TestCase的子类上
@ddt
class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com/"

    # data表示data是直接提供的。注意data里的参数我写了函数get_test_data()的返回值，并且以*为前缀，代表返回的是可变参数。
    # unpack表示，对于每一组数据，如果它的值是list或者tuple，那么就分拆成独立的参数
    @data(*get_test_data('test_baidu.xlsx'))
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
    # get_test_data('test_baidu.xlsx')
