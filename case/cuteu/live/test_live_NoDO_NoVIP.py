

#无钻石送礼物操作
from base.base_action import BaseAction
from base.base_driver import setdriver
from pageproject.cuteu.live.live_page import LivePage
from case.cuteu.common import Publicservice as login



class Testlive:
    def test_live_page(self, init_driver):
        login().mobile_phone(init_driver['driver'], 13100000002)
        # 导航栏进入直播页面
        LivePage(init_driver['driver']).live_loc()
    def test_user_live(self,init_driver):
        # 点击正在直播的主播
        LivePage(init_driver['driver']).user_live()

    def test_room_gift(self, init_driver):

        # 送礼物操作
        LivePage(init_driver['driver']).room_gift()
        # 选择礼物
        LivePage(init_driver['driver']).room_gift_choose()
        # 发送礼物
        LivePage(init_driver['driver']).room_gift_send()
        assert LivePage(init_driver['driver']).room_gift_assert()
        BaseAction(init_driver['driver']).back()
        BaseAction(init_driver['driver']).back()
        BaseAction(init_driver['driver']).back()

if __name__ == '__main__':
    x=setdriver().runapp()
    w=Testlive()