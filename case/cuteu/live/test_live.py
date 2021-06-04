import os
import sys
import time

from base.base_action import BaseAction
from base.base_driver import setdriver
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
        logger.info("进入直播页面元素caes结束")

    def test_user_live(self,init_driver):
        logger.info("进入主播直播间cese开始")
        #进入第一个主播直播间
        # NoUser = LivePage(init_driver['driver']).user_live()
        # if NoUser == None:
        #     logger.info("进入直播间时间过长，跳过")
        # else:
       # 进入第一个主播直播间
        LivePage(init_driver['driver']).user_live()

        # 判断是否加载时间过长
        a = LivePage(init_driver['driver']).room_loading(init_driver)
        if a==False:
            #直播间操作
            #主播名字
            LivePage(init_driver['driver']).room_username()
            #关注
            LivePage(init_driver['driver']).username_follow()
            #举报
            LivePage(init_driver['driver']).username_report()
            BaseAction(init_driver['driver']).back()
            #点击主播头像
            LivePage(init_driver['driver']).username_head()
            BaseAction(init_driver['driver']).back()
            #点击主播名字
            LivePage(init_driver['driver']).room_username()
            LivePage(init_driver['driver']).username_close()

            #点击钻石按钮，奖池
            LivePage(init_driver['driver']).room_damond()
            LivePage(init_driver['driver']).room_damond()

            #点击公告
            LivePage(init_driver['driver']).room_notice()
            BaseAction(init_driver['driver']).back()


            #贡献榜
            LivePage(init_driver['driver']).room_user(init_driver)

            #发送消息
            LivePage(init_driver['driver']).room_msg()

            #送礼物操作
            LivePage(init_driver['driver']).room_gift()
                #选择礼物
            LivePage(init_driver['driver']).room_gift_choose()
                #发送礼物
            LivePage(init_driver['driver']).room_gift_send()
            BaseAction(init_driver['driver']).back()
            #充值钻石
            LivePage(init_driver['driver']).room_gift_recharge()
            BaseAction(init_driver['driver']).back()
            BaseAction(init_driver['driver']).back()

            #关闭直播间
            LivePage(init_driver['driver']).room_exit()
            logger.info("进入主播直播间cese结束")
        else:
            logger.info("无法进入直播间")

if __name__ == '__main__':
    x=setdriver().runapp()
    w=Testmsg()


