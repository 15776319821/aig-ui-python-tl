# -*- coding:utf-8 -*-
# @Time     :2021/4/28 19:10
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :common.py
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

class Publicservice:
    def fast_register(self,init_driver):
        '''快速注册按钮'''
        b = BaseAction(init_driver).is_elementloc(LoginLoc.submit_loc)
        if b:
            LoginPage(init_driver).first_install_warrant()
        else:
            logger.info('没有开屏授权的弹窗')
        LoginPage(init_driver).fast_register()
        a = BaseAction(init_driver).is_elementloc(LoginLoc.male_loc)
        if a:
            LoginPage(init_driver).perfect_information()
        else:
            logger.info('不是快速注册的流程，是直接登录')

    def google_login(self,init_driver):
        '''谷歌登录'''
        b = BaseAction(init_driver).is_elementloc(LoginLoc.submit_loc)
        if b:
            LoginPage(init_driver).first_install_warrant()
        else:
            logger.info('没有开屏授权的弹窗')
        LoginPage(init_driver).google_login()
        a = BaseAction(init_driver).is_elementloc(LoginLoc.male_loc)
        if a:
            LoginPage(init_driver).perfect_information()
        else:
            logger.info('不是谷歌注册的流程，是直接登录')

    def facebook_login(self,init_driver):
        '''facebook登录按钮'''
        b = BaseAction(init_driver).is_elementloc(LoginLoc.submit_loc)
        if b:
            LoginPage(init_driver).first_install_warrant()
        else:
            logger.info('没有开屏授权的弹窗')
        LoginPage(init_driver).facebook_login()
        a = BaseAction(init_driver).is_elementloc(LoginLoc.male_loc)
        if a:
            LoginPage(init_driver).perfect_information()
        else:
            logger.info('不是facebook注册的流程，是直接登录')

    def mobile_phone(self,init_driver,mobile):
        '''这个是手机号登录方式'''
        b = BaseAction(init_driver).is_elementloc(LoginLoc.submit_loc)
        if b:
            LoginPage(init_driver).first_install_warrant()
        else:
            logger.info('没有开屏授权的弹窗')
        LoginPage(init_driver).mobile_phone(mobile)
        a = BaseAction(init_driver).is_elementloc(LoginLoc.male_loc)
        if a:
            LoginPage(init_driver).perfect_information()
        else:
            logger.info('不是手机号注册的流程，是直接登录')
    def loginout(self,init_driver):
        LoginoutPage(init_driver).loginout()