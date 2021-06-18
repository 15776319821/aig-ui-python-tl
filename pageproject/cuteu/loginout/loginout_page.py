# -*- coding:utf-8 -*-
# @Time     :2021/6/12 17：58
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :loginout_page.py
# @Software :PyCharm

import os
import sys
sys.path.append(os.getcwd())
import time
from elementloc.cuteu.loginout.loginout_loc import LoginoutLoc
from base.base_action import BaseAction
from base.base_log import logger

class LoginoutPage(BaseAction):
    def loginout(self):
        self.click_element(LoginoutLoc.us_loc, '点击一级模块--我的')
        self.click_element(LoginoutLoc.set_loc, '点击设置')
        self.click_element(LoginoutLoc.loginout_loc, '点击退出登录')
        self.click_element(LoginoutLoc.surt_loc, '点击确定退出')

'''
        a = self.is_elementloc(LoginoutLoc.us_loc)
        if a == True:
            self.click_element(LoginoutLoc.us_loc,'点击一级模块--我的')
            self.click_element(LoginoutLoc.set_loc,'点击设置')
            self.click_element(LoginoutLoc.loginout_loc,'点击退出登录')
            self.click_element(LoginoutLoc.surt_loc,'点击确定退出')
        else:
            self.back()
            if a == True:
                self.click_element(LoginoutLoc.us_loc, '点击一级模块--我的')
                self.click_element(LoginoutLoc.set_loc, '点击设置')
                self.click_element(LoginoutLoc.loginout_loc, '点击退出登录')
                self.click_element(LoginoutLoc.surt_loc, '点击确定退出')
            else:
                self.back()
                if a == True:
                    self.click_element(LoginoutLoc.us_loc, '点击一级模块--我的')
                    self.click_element(LoginoutLoc.set_loc, '点击设置')
                    self.click_element(LoginoutLoc.loginout_loc, '点击退出登录')
                    self.click_element(LoginoutLoc.surt_loc, '点击确定退出')
                else:
                    self.back()
'''