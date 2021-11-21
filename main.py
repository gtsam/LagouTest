# coding=utf-8

import importlib.util
import unittest
import os
from .common.html_reporter import GenerateReport
from .tests.test_to_run import TestToRun
from .tests.itesting_test import ITestingTest


# 解析tests文件夹，并且返回module的字符串列表
def get_module_name_string(file_dir):
    return_list = []
    for root, dirs, file in os.walk(file_dir):
        for i in file:
            if not (i.endswith('__init__.py') or i.endswith('.pyc')):
                mod = 'tests.' + i.split('.')[0]
                # f = os.path.join(root, i)
                # mod = 'tests.' + f.split('\\tests\\')[1].replace('.py', '').replace('\\', '.')
                return_list.append(mod)

    return return_list


if __name__ == '__main__':
    # 运行指定文件夹下的测试用例
    # ----------------------------------------------------
    # # 定义suites
    # suites = unittest.TestSuite()
    # # 获取所有的module的string，类似package.mod的方式
    # return_list = get_module_name_string(os.path.join(os.path.dirname(__file__), 'tests'))
    # print('lllllllll', return_list)
    #
    # # 遍历每个mod string，import并且把它加入test case中来
    # for mod_string in return_list:
    #     m = importlib.import_module(mod_string)
    #     print('mmmmmmmmmmmmm', m)
    #     test_case = unittest.TestLoader().loadTestsFromModule(m)
    #     suites.addTests(test_case)
    # ----------------------------------------------------

    # 动态查找测试用例运行
    # ----------------------------------------------------
    # loader = unittest.defaultTestLoader
    # 生成测试suites
    # suites = loader.discover(os.path.join(os.path.dirname(__file__), 'tests'), pattern='*.py', top_level_dir=os.path.dirname(__file__))
    # ----------------------------------------------------

    # 按需组装测试用例
    # ----------------------------------------------------
    # # 定义一个测试用例集
    # suites = unittest.TestSuite()
    # suites.addTests(map(TestToRun, ['testAssertNotEqual', 'testAssertEqual']))
    # suites.addTest(ITestingTest('equal_test'))
    # ----------------------------------------------------

    # 指定runner为TextTestRunner
    # runner = unittest.TextTestRunner(verbosity=2)
    # 运行suites
    # runner.run(suites)

    # 使用测试报告模块生成测试报告
    # ----------------------------------------------------
    suite = unittest.defaultTestLoader.discover(os.path.join(os.path.dirname(__file__),"tests"),
                                                pattern='*.py',top_level_dir=os.path.dirname(__file__))
    html_report = GenerateReport()
    html_report.generate_report(suite)
    # ----------------------------------------------------