import os
import sys
import time

from base.base_action import BaseAction
from pageproject.cuteu.live.live_page import LivePage
sys.path.append(os.getcwd())
from base.base_log import logger

class Testmsg:
    def test_live(self,init_driver):
        logger.info("进入直播页面，点击一级页面元素")
        #进入直播页面
        LivePage(init_driver['driver']).live_loc()
        #点击直播-关注
        LivePage(init_driver['driver']).top_follow()
        LivePage(init_driver['driver']).top_live()
        #进入第一个主播直播间
        LivePage(init_driver['driver']).user_live()
        #直播间操作
        LivePage(init_driver['driver']).room_username()
        #贡献榜
        LivePage(init_driver['driver']).room_user()
        BaseAction(init_driver['driver']).back()

        #点击关注
        LivePage(init_driver['driver']).room_follow()
        LivePage(init_driver['driver']).username_head()
        BaseAction(init_driver['driver']).back()
        LivePage(init_driver['driver']).username_report()
        BaseAction(init_driver['driver']).back()
        LivePage(init_driver['driver']).username_follow()
        LivePage(init_driver['driver']).username_close()

        #点击钻石按钮，奖池
        LivePage(init_driver['driver']).room_damond()
        LivePage(init_driver['driver']).room_damond()
        #送礼物操作
        LivePage(init_driver['driver']).room_notice()
        BaseAction(init_driver['driver']).back()
        LivePage(init_driver['driver']).room_gift()
        LivePage(init_driver['driver']).room_gift_choose()
        LivePage(init_driver['driver']).room_gift_send()
        LivePage(init_driver['driver']).room_gift_recharge()
        BaseAction(init_driver['driver']).back()
        #提示赠送礼物
        LivePage(init_driver['driver']).room_sendgift()
        #关闭直播间
        LivePage(init_driver['driver']).room_exit()




