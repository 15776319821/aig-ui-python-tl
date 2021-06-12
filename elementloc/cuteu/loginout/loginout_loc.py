# -*- coding:utf-8 -*-
# @Time     :2021/6/12 17:56
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :login_loc.py
# @Software :PyCharm

from selenium.webdriver.common.by import By

class LoginoutLoc():
    #一级tab—我的
    us_loc = (By.ID,"com.cuteu.videochat:id/btnTabMine")
    #右上角的设置
    set_loc = (By.ID,"com.cuteu.videochat:id/imgSet")
    #设置—退出登录'
    loginout_loc = (By.ID,"com.cuteu.videochat:id/settingQuit")
    #设置—关于我们—关于我们
    surt_loc = (By.ID,"android:id/button1")