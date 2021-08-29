# coding=utf-8
import json
import unittest
import pytest
import requests


@pytest.mark.lagou
class TestLaGou(unittest.TestCase):
    def setUp(self):
        self.s = requests.Session()
        self.url = 'https://www.lagou.com'

    def test_visit_lagou(self):
        result = self.s.get(self.url)
        assert result.status_code == 200
        unittest.TestCase.assertIn(self, '拉勾', result.text)

    def test_get_new_message(self):
        # 此处需要一个方法登录获取登录的cookie，但因我们无法知道拉勾登录真实的API，故采用此方式登录
        message_url = 'https://gate.lagou.com/v1/entry/message/newMessageList'
        cookie = {
            'cookie': 'edu_gate_login_token=$$$EDU_eyJraWQiOiIyZDBhODJmMi05ZDk1LTQ5MWItYmNiMC03ZjRmZWIxOWM4ZTMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJ0Z3QiOiJfQ0FTX1RHVF9UR1QtMDdmNmU3NTlmNTQzNDc4MWEyM2UxMjM4ZmI2OWVjYzgtMjAyMTA4MDExNDA1NTItX0NBU19UR1RfIiwic3ViIjoiMTk3NzQ1MjEiLCJpcCI6IjIyMi42OS4xNTUuNDAiLCJpc3MiOiJlZHUubGFnb3UuY29tIiwidG9rZW5UeXBlIjoxLCJleHAiOjE2Mjg0MDI3NTIsImlhdCI6MTYyNzc5Nzk1Mn0.Xk2RvFNEm1Q89rfa0U_ivIylTh7Kg72UjR3qg7xStH38J4e1uIize3zL7MkkuWfmDw618Za2IFjnyS1663qNoEvtBV62cMw--rQ6Dw_gEStvfq2ppMLCkEL6jIiVA89RgRoTy6-LT9q8ngJIZXvlGGsnVqo_4lNo9LmIHICpuRzDvGXOcTrCPVZhN-VGmZ65idbpNUtNRIYUR3wxUn9Ss6g7_qs3zSekzVrGmW0FTyv0hP1hs_3IavjY_sYe5R2mKduR1hZbX0lbNzMbgPVIGzgok6gRMG7OxdHW3bu64rjVqLRUhnSnWRn6jRG1bUekdXL2Z1Dez3re8d8ytJcrTA; gate_login_token=675d15a5a57e055e52ba092c6403b440232674b85e5ffb7e38f46ee293da7412;'}
        headers = {'x-l-req-header': '{deviceType: 9}'}
        # 直接带登录态发送请求
        result = self.s.get(message_url, cookies=cookie, headers=headers)
        assert result.status_code == 200
        assert json.loads(result.content)['message'] == '成功'

    def tearDown(self):
        self.s.close()

if __name__ == "__main__":
    unittest.main(verbosity=2)