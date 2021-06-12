# -*- coding:utf-8 -*-
# @Time     :2021/4/25 21:51
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :login_page.py
# @Software :PyCharm

import os
import sys
sys.path.append(os.getcwd())
import time
from elementloc.cuteu.login.login_loc import LoginLoc
from base.base_action import BaseAction
from base.base_log import logger

class LoginPage(BaseAction):
    #首次安装app进入登录页面之前的授权
    def first_install_warrant(self):
        self.click_element(LoginLoc.submit_loc,"点击授权许可")
        self.click_element(LoginLoc.location_allow_loc,"同意定位")
        self.click_element(LoginLoc.memory_allow_loc,"同意存储")
    #选择登录方式—快速注册
    def fast_register(self):
        self.click_element(LoginLoc.fast_register_loc,"点击快速注册")
    #选择登录方式—谷歌登录
    def google_login(self):
        self.click_element(LoginLoc.google_login_loc,"点击谷歌登录")
        a = self.is_elementloc(LoginLoc.select_google_loc)
        if a :
            self.click_elements(LoginLoc.select_google_loc,0,"如果有多个账号就选择第一个账号")
        else:
            logger.info('不需要选择谷歌登陆账号')
        b = self.is_elementloc(LoginLoc.confirm_loc)
        if b :
            self.click_element(LoginLoc.confirm_loc,"点击绑定谷歌账号弹窗的确定")
        else:
            logger.info('这条case不是绑定谷歌账号的流程')
    #选择登录方式—facebook
    def facebook_login(self):
        self.click_element(LoginLoc.facebook_longin_loc,"点击facebook登录")
        self.click_element(LoginLoc.select_facebook_loc,"进入facebookH5页面进行登录")
        a = self.is_elementloc(LoginLoc.confirm_loc)
        if a :
            self.click_element(LoginLoc.confirm_loc,"点击绑定facebook账号弹窗的确定")
        else:
            logger.info('这条case不是绑定facebook账号的流程')
    #选择手机号登录方式
    def mobile_phone(self,number):
        self.click_element(LoginLoc.mobile_phone_loc,"点击手机号登录")
        self.click_element(LoginLoc.input_phone_loc,"点击手机号输入框")
        self.input_text(LoginLoc.input_phone_loc,number,"手机号输入框中输入大陆手机号")
        time.sleep(1)
        self.click_element(LoginLoc.send_number_loc,"点击发送验证码")
        self.click_element(LoginLoc.input_number_loc,"点击验证码的输入框")
        self.input_text(LoginLoc.input_number_loc,123456,"验证码输入框输入固定验证码")
        time.sleep(1)
        self.back()
        self.click_element(LoginLoc.phone_next_loc,"点击下一步")
        a = self.is_elementloc(LoginLoc.confirm_loc)
        if a :
            self.click_element(LoginLoc.confirm_loc,"点击绑定手机号弹窗的确定")
        else:
            logger.info('这条case不是绑定手机号的流程')
    #创建人物信息的流程
    def perfect_information(self):
        self.click_element(LoginLoc.male_loc,"性别：男")
        self.click_element(LoginLoc.gender_next_loc,"性别页面下一步")
        self.click_element(LoginLoc.nickname_next_loc,"昵称页面下一步")
        self.click_element(LoginLoc.birthday_next_loc,"生日下一步")
        self.click_element(LoginLoc.photo_next_loc,"上传头像页下一步")
        self.click_element(LoginLoc.purpose_next_loc,"交友目的-下一步")
        a = self.is_elementloc(LoginLoc.recording_loc)
        if a is True:
            self.click_element(LoginLoc.recording_loc,"录音授权")
            self.click_element(LoginLoc.camera_loc,"摄像头授权")
            self.click_element(LoginLoc.iknow_loc, "点击我知道了")
        else:
            self.click_element(LoginLoc.iknow_loc,"点击我知道了")
