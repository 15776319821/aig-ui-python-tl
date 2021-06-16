import os
import sys

from case.cuteu.conftest import init_driver
from elementloc.cuteu.live.live_loc import LiveLoc
sys.path.append(os.getcwd())
import time
from base.base_action import BaseAction, logger


class LivePage(BaseAction):
    '''直播页面一级页面操作'''
    def live_loc(self):
        self.click_element(LiveLoc.live_loc, "导航栏直播按钮")

    def top_follow(self):
        self.click_element(LiveLoc.top_follow, "关注")

    def top_live(self):
        self.click_element(LiveLoc.top_live, "直播")
    def top_live_assert(self):
        return self.is_exist(LiveLoc.user_live)

    def user_live_assert(self):
        time.sleep(10)
        if self.is_exist(LiveLoc.user_live):
            if self.is_exist(LiveLoc.room_loading) != True:
                return True
        else:
            return False

    def user_live(self):
            self.click_element(LiveLoc.user_live, "第一个直播主播")

    '''直播间内元素'''
    def room_username(self):
        self.click_element(LiveLoc.room_username, "主播名字")
    def room_username_assert(self):
        return self.is_exist(LiveLoc.username_head)

    def username_head(self):
        self.click_element(LiveLoc.username_head, "点击主播头像")
    def username_head_assert(self):
        return self.is_exist(LiveLoc.username_head_assert)

    def username_report(self):
        self.click_element(LiveLoc.username_report, "点击举报主播")
    def username_report_assert(self):
        return self.is_exist(LiveLoc.username_report)

    def username_follow(self):
        self.click_element(LiveLoc.username_follow, "点击关注主播")
    def username_follow_assert(self):
        return self.is_exist(LiveLoc.username_follow)

    def username_close(self):
        self.click_element(LiveLoc.username_close, "点击关闭主播个人信息")
    def username_close_assert(self):
        return self.is_exist(LiveLoc.username_close)

    def room_damond(self):
        self.click_element(LiveLoc.room_damond, "钻石按钮")
    def room_damond_assert(self):
        return  self.is_exist(LiveLoc.room_damond_assert)

    def room_notice(self):
        self.click_element(LiveLoc.room_notice, "公告")
    def room_notice_assert(self):
        return self.is_exist(LiveLoc.room_notice_assert)

    def room_msg(self):
        self.click_element(LiveLoc.room_msg, "发送消息")
        # self.input_text(LiveLoc.room_msg,"你好啊","发送消息")
        self.click_element(LiveLoc.room_sendmsg, "点击发送")


    def room_gift(self):
        self.click_element(LiveLoc.room_gift, "礼物")
    def room_gift_choose(self):
        self.click_element(LiveLoc.room_gift_choose, "选择礼物")
    def room_gift_send(self):
        self.click_element(LiveLoc.room_gift_send, "发送礼物")
    def room_gift_assert(self):
        return self.is_exist(LiveLoc.room_gift_recharge)

    def room_gift_recharge(self):
        self.click_element(LiveLoc.room_gift_recharge, "充值钻石")

    def room_exit(self):
        self.click_element(LiveLoc.room_exit, "关闭直播间")

    def room_user(self,init_driver):
            self.click_element(LiveLoc.room_user, "贡献榜")
            BaseAction(init_driver['driver']).back()

#暂时未使用

    def room_sendgift(self):
        self.click_element(LiveLoc.room_sendgift, "提示赠送礼物")
    #直播间加载
    # def room_loading(self,init_driver):
    #     time.sleep(15)
    #     loadiong = self.is_elementloc(LiveLoc.room_loading)
    #     if loadiong == True:
    #         BaseAction(init_driver['driver']).back()
    #         logger.info("加载时间过长，结束")
    #     else:
    #         return False


