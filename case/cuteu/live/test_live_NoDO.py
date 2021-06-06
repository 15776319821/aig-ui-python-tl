

#无钻石送礼物操作
from base.base_action import BaseAction
from pageproject.cuteu.live.live_page import LivePage


def test_room_gift(self, init_driver):
    # 有钻石送礼物操作
    # 送礼物操作
    LivePage(init_driver['driver']).room_gift()
    # 选择礼物
    LivePage(init_driver['driver']).room_gift_choose()
    # 发送礼物
    LivePage(init_driver['driver']).room_gift_send()
    assert LivePage(init_driver['driver']).room_gift_recharge()