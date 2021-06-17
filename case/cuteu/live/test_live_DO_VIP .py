import os
import sys
import time

from base.base_action import BaseAction
from base.base_driver import setdriver
from pageproject.cuteu.live.live_page import LivePage
sys.path.append(os.getcwd())
from base.base_log import logger
from case.cuteu.common import Publicservice as login

class Testlive:
    def test_live_page(self,init_driver):
        login.mobile_phone(mobile='13100000005')
        #导航栏进入直播页面
        LivePage(init_driver['driver']).live_loc()

    def test_live_follow(self,init_driver):
        #点击关注
        LivePage(init_driver['driver']).top_follow()

    def test_live(self,init_driver):
        #点击直播
        LivePage(init_driver['driver']).top_live()
        assert LivePage(init_driver['driver']).top_live_assert()

    def test_user_live(self,init_driver):
        # 点击正在直播的主播
        LivePage(init_driver['driver']).user_live()

        #直播间内操作
        #主播名字
    def test_username(self,init_driver):
        LivePage(init_driver['driver']).room_username()
        assert LivePage(init_driver['driver']).room_username_assert()

    def test_username_follow(self,init_driver):
        #关注
        LivePage(init_driver['driver']).room_username()
        LivePage(init_driver['driver']).username_follow()
        assert LivePage(init_driver['driver']).username_follow_assert()

    def test_username_report(self,init_driver):
        #举报
        LivePage(init_driver['driver']).username_report()
        BaseAction(init_driver['driver']).back()
        assert LivePage(init_driver['driver']).username_report_assert()

    def test_username_head(self,init_driver):
        #点击主播头像
        LivePage(init_driver['driver']).username_head()
        time.sleep(5)
        BaseAction(init_driver['driver']).back()
        assert LivePage(init_driver['driver']).username_head_assert()

    def test_room_damond(self,init_driver):
        #点击钻石按钮，奖池
        LivePage(init_driver['driver']).room_damond()
        time.sleep(6)
        assert LivePage(init_driver['driver']).room_damond_assert()

    def test_room_notice(self,init_driver):
        #点击公告
        LivePage(init_driver['driver']).room_notice()
        assert LivePage(init_driver['driver']).room_notice_assert()
        BaseAction(init_driver['driver']).back()

    def test_room_msg(self,init_driver):
        #发送消息
        LivePage(init_driver['driver']).room_msg()
        BaseAction(init_driver['driver']).back()

    def test_room_gift(self,init_driver):
        #有钻石送礼物操作
        #送礼物操作
        LivePage(init_driver['driver']).room_gift()
            #选择礼物
        LivePage(init_driver['driver']).room_gift_choose()
            #发送礼物
        LivePage(init_driver['driver']).room_gift_send()
        time.sleep(6)

    def test_room_recharge(self,init_driver):
        #充值钻石
        LivePage(init_driver['driver']).room_gift()
        LivePage(init_driver['driver']).room_gift_recharge()
        BaseAction(init_driver['driver']).back()
        BaseAction(init_driver['driver']).back()

    def test_room_user(self, init_driver):
        # 贡献榜
        LivePage(init_driver['driver']).room_user(init_driver)

    def test_room_exit(self,init_driver):
        #关闭直播间
        LivePage(init_driver['driver']).room_exit()
        logger.info("进入主播直播间cese结束")



if __name__ == '__main__':
    x=setdriver().runapp()
    w=Testlive()


