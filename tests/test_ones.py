# -*- coding: utf-8 -*-
import pytest
from ..pages.ones import OneAI  # 需要写相对路径，不然pytest执行的时候找不到对应的目录

class TestOneAI:
    # 注意，需要email和密码需要更改成你自己的账户密码
    @pytest.mark.parametrize('login_data, project_name, target_page', [({"password": "Dean_3170833073", "email": "923210866@qq.com"}, {"project_name":"VIPTEST"}, {"target_page": "https://ones.ai/project/#/home/project"})])
    def test_project_name_txt(self, login_data, project_name, target_page):
        print(login_data)
        one_page = OneAI(login_data, target_page)
        actual_project_name = one_page.get_project_name()
        assert actual_project_name == project_name["project_name"]

if __name__ == '__main__':
    one_ai = TestOneAI()
    one_ai.test_project_name_txt()