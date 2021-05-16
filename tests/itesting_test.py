# coding=utf-8

import unittest
flag = False

# 测试类必须要继承TestCase类
class ITestingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('整个测试类只执行一次 -- Start')

    def setUp(self):
        print('每个测试开始前执行一次')

    # 测试用例默认以test开头
    @unittest.skip('没有任何原因，忽略运行')
    def equal_test(self):
        self.assertEqual(1, 1)

    @unittest.skipIf(flag == True, 'flag为True则skip')
    def test_not_equal(self):
        self.assertNotEqual(1, 0)

    @unittest.skipUnless(flag == True, 'flag为False则skip')
    def test_not_equal1(self):
        self.assertNotEqual(1, 0)

    @unittest.expectedFailure
    def test_not_equal2(self):
        self.assertNotEqual(1, 1)

    def tearDown(self):
        print('每个测试结束后执行一次')

    @classmethod
    def tearDownClass(cls):
        print('整个测试类只执行一次 -- End')
