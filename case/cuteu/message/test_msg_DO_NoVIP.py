'''消息页面，非会员有钻场景拆解'''
from base.base_action import BaseAction
from pageproject.cuteu.message.msg_page import MsgPage


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

