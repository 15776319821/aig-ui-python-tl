# -*- coding:utf-8 -*-
# @Time     :2021/6/24 14:50
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :test_login_NoDO_NoVIP.py
# @Software :PyCharm
import os
import sys
sys.path.append(os.getcwd())
import time
from pageproject.cuteu.login.login_page import LoginPage
from base.base_log import logger
from elementloc.cuteu.login.login_loc import LoginLoc
from base.base_action import BaseAction
from pageproject.cuteu.loginout.loginout_page import LoginoutPage
from case.cuteu.common import Publicservice as login

class Testlogin():
    def test_login(self,init_driver):
        login().mobile_phone(init_driver['driver'],13100000002)