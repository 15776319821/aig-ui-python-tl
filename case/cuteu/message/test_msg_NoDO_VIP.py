'''消息页面，会员无钻场景拆解'''
from base.base_action import BaseAction
from pageproject.cuteu.message.msg_page import MsgPage


def test_user_msg(self, init_driver):
    # 发送消息
    MsgPage(init_driver['driver']).user_msg()
    MsgPage(init_driver['driver']).user_send()

def test_user_voice(self, init_driver):
    # 发送语音消息
    MsgPage(init_driver['driver']).user_voice()
    assert MsgPage(init_driver['driver']).user_voice_assert()
    MsgPage(init_driver['driver']).voice_send()

def test_user_img(self, init_driver):
    # 点击选择图片
    MsgPage(init_driver['driver']).user_img()
    assert MsgPage(init_driver['driver']).user_img_assert()
    MsgPage(init_driver['driver']).user_img_choose()
    assert MsgPage(init_driver['driver']).user_photo_assert()
    # 点击小秘密按钮
    MsgPage(init_driver['driver']).user_secret()
    MsgPage(init_driver['driver']).user_secret()
    # 发送图片
    MsgPage(init_driver['driver']).img_send()

def test_user_video(self, init_driver):
    # 点击视频聊天
    MsgPage(init_driver['driver']).user_video()
    assert MsgPage(init_driver['driver']).close_diamond_assert()
    BaseAction(init_driver['driver']).back()

def test_user_call(self, init_driver):
    # 点击语音聊天
    MsgPage(init_driver['driver']).user_call()
    assert MsgPage(init_driver['driver']).close_diamond_assert()
    BaseAction(init_driver['driver']).back()


def test_user_gift(self, init_driver):
    # 礼物按钮
    MsgPage(init_driver['driver']).user_gift()
    MsgPage(init_driver['driver']).gift_choose()
    MsgPage(init_driver['driver']).gift_send()
    assert MsgPage(init_driver['driver']).gitf_close_diamond_assert()
    BaseAction(init_driver['driver']).back()
    BaseAction(init_driver['driver']).back()


def test_user_red(self, init_driver):
    # 点击红包按钮
    MsgPage(init_driver['driver']).user_red()
    assert MsgPage(init_driver['driver']).user_red_assert()
    MsgPage(init_driver['driver']).red_custom()
    MsgPage(init_driver['driver']).red_input()
    BaseAction(init_driver['driver']).back()
    MsgPage(init_driver['driver']).red_upload()
    MsgPage(init_driver['driver']).red_recharge()
    BaseAction(init_driver['driver']).back()
    MsgPage(init_driver['driver']).red_send()
    assert MsgPage(init_driver['driver']).gitf_close_diamond_assert()
    BaseAction(init_driver['driver']).back()
    BaseAction(init_driver['driver']).back()
