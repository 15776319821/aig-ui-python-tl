# -*- coding:utf-8 -*-
# @Time     :2021/6/9 20:12
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :test_profile_NoDO_NoVIP.py
# @Software :PyCharm

import os
import sys
sys.path.append(os.getcwd())
from pageproject.cuteu.profile.profile_page import ProfilePage
from base.base_log import logger
from case.cuteu.common import Publicservice
import time

class Testprofile():
    def test_profile_top(self,init_driver):
        # a = Publicservice()
        # a.mobile_phone(init_driver['driver'],13100000002)
        time.sleep(3)
        '''这是个人空间页顶部位置的所有操作'''
        ProfilePage(init_driver['driver']).into_profile()
        ProfilePage(init_driver['driver']).heart()
        ProfilePage(init_driver['driver']).voice()
        ProfilePage(init_driver['driver']).select_photo()
        ProfilePage(init_driver['driver']).profile_swipeToRight()
        ProfilePage(init_driver['driver']).profile_swipeToLeft()
        ProfilePage(init_driver['driver']).phone_novip()
        ProfilePage(init_driver['driver']).call_video_novip()
    def test_profile_show(self,init_driver):
        '''这是show签下的所有操作'''
        ProfilePage(init_driver['driver']).switch_show()
        ProfilePage(init_driver['driver']).profile_swipeToUP()
        ProfilePage(init_driver['driver']).show_voice()

    def test_profile_information(self,init_driver):
        '''这是消息页签下的所有操作'''
        #ProfilePage(init_driver['driver']).profile_swipeToDown()
        ProfilePage(init_driver['driver']).switch_information()
        ProfilePage(init_driver['driver']).information_invite()