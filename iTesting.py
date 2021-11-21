# coding=utf-8
import pytest
flag = False

class TestSample(object):
    # 测试用例默认以test开头
    def test_equal(self):
        assert 1 == 0

    def test_not_equal(self):
        assert 1 != 0

    @pytest.mark.skip(reason='测试pytest忽略此测试用例')
    def test_equal1(self):
        assert 1 == 1

    @pytest.mark.skipif(flag == True, reason='by condition')
    def test_equal2(self):
        assert 1 == 1

    @pytest.mark.skipif(flag == False, reason='by condition1')
    def test_equal3(self):
        assert 1 == 1

    # 使用了pytest里的参数化
    @pytest.mark.parametrize('login_data, project_name', [({"password": "iTestingIsGood", "email": "pleasefollowiTesting@outlook.com"}, {"project_name":"VIPTEST"})])
    def test_merge_api_ui(self, login_data, project_name):
        assert login_data['password'] == 'iTestingIsGood'
        assert login_data['email'] == 'pleasefollowiTesting@outlook.com'
        assert project_name['project_name'] == 'VIPTEST'


if __name__ == '__main__':
    sample = TestSample()
    sample.test_merge_api_ui()