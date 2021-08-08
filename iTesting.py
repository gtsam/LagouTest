# coding=utf-8
import pytest

class TestSample(object):
    # 测试用例默认以test开头
    def test_equal(self):
        assert 1 == 1

    def test_not_equal(self):
        assert 1 != 0