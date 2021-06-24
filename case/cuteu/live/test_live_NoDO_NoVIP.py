# -*- coding:utf-8 -*-

#无钻石送礼物操作
from base.base_action import BaseAction
from base.base_driver import setdriver
from pageproject.cuteu.live.live_page import LivePage
from case.cuteu.common import Publicservice as login
import time



class Testlive:
    def test_live_page(self, init_driver):
        # login().mobile_phone(init_driver['driver'], 13100000002)
        # 导航栏进入直播页面
        time.sleep(3)
        LivePage(init_driver['driver']).live_loc()
        time.sleep(3)
    def test_user_live(self,init_driver):
        # 点击正在直播的主播
        LivePage(init_driver['driver']).user_live()
        time.sleep(3)

    def test_room_gift(self, init_driver):

        # 送礼物操作
        LivePage(init_driver['driver']).room_gift()
        # 选择礼物
        LivePage(init_driver['driver']).room_gift_choose()
        # 发送礼物
        LivePage(init_driver['driver']).room_gift_send()
        # assert LivePage(init_driver['driver']).room_gift_assert()
        time.sleep(1)
        BaseAction(init_driver['driver']).back()
        time.sleep(2)
        BaseAction(init_driver['driver']).back()
        time.sleep(2)
        BaseAction(init_driver['driver']).back()

if __name__ == '__main__':
    x=setdriver().runapp()
    w=Testlive()