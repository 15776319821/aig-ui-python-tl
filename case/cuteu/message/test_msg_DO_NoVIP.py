# -*- coding:utf-8 -*-
'''消息页面，非会员有钻场景拆解'''
from base.base_action import BaseAction
from base.base_driver import setdriver
from pageproject.cuteu.message.msg_page import MsgPage
from case.cuteu.common import Publicservice as login
from base.base_log import logger
import time

class Testmsg():
    def test_msg(self, init_driver):
        # login().mobile_phone(init_driver['driver'],13100000004)
        time.sleep(3)
        # 进入消息页面
        logger.info("进入消息页面，点击一级页面元素")
        MsgPage(init_driver['driver']).msg_jump()
        assert MsgPage(init_driver['driver']).msg_jump_assert()

    def test_CuteU_Msg_VIP(self, init_driver):
        logger.info("用户主播聊天case开始")
        # 点击消息-点击消息页面第一个用户
        MsgPage(init_driver['driver']).CuteU_user()
        # assert MsgPage(init_driver['driver']).CuteU_user_assert()

    def test_user_msg(self, init_driver):
        # 发送消息
        MsgPage(init_driver['driver']).user_msg()
        MsgPage(init_driver['driver']).user_send()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()

    def test_user_voice(self, init_driver):
        # 发送语音消息
        MsgPage(init_driver['driver']).user_voice()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()

    def test_user_img(self, init_driver):
        # 点击选择图片
        MsgPage(init_driver['driver']).user_img()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()

    def test_user_video(self, init_driver):
        # 点击视频聊天
        MsgPage(init_driver['driver']).user_video()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()

    def test_user_call(self, init_driver):
        # 点击语音聊天
        MsgPage(init_driver['driver']).user_call()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()


    def test_user_gift(self, init_driver):
        # 礼物按钮
        MsgPage(init_driver['driver']).user_gift()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()

    def test_user_red(self, init_driver):
        # 点击红包按钮
        MsgPage(init_driver['driver']).user_red()
        assert MsgPage(init_driver['driver']).close_vip_assert()
        MsgPage(init_driver['driver']).close_vip()
        BaseAction(init_driver['driver']).back()

if __name__ == '__main__':
    x=setdriver().runapp()
    w=Testmsg()
