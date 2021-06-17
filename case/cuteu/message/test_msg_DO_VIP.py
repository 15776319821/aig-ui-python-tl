# -*- coding:utf-8 -*-
# 引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
from base.base_action import BaseAction
from base.base_driver import setdriver
sys.path.append(os.getcwd())
from pageproject.cuteu.message.msg_page import MsgPage
from case.cuteu.common import Publicservice as login
from base.base_log import logger
"""
008613100000002  非会员无钻
008613100000003   会员无钻
008613100000004   非会员500000钻
008613100000005   会员500000钻
"""
class Testmsg():
    def test_msg(self,init_driver):
        login().mobile_phone(init_driver['driver'], 13100000005)
        #进入消息页面
        logger.info("进入消息页面，点击一级页面元素")
        MsgPage(init_driver['driver']).msg_jump()
        assert MsgPage(init_driver['driver']).msg_jump_assert()

    def test_news_jump(self,init_driver):
        #点击消息-互动消息
        MsgPage(init_driver['driver']).news_jump()
        assert MsgPage(init_driver['driver']).news_jump_assert()
        logger.info("进入消息页面跳转case结束")


        '''互动消息页面'''
    def test_news_page(self,init_driver):
        logger.info("互动消息页面case开始")
        # # 点击互动通知用户头像 点击返回
        # MsgPage(init_driver['driver']).newspage_head()
        # BaseAction(init_driver['driver']).back()
        # #点击互动通知第一条消息 点击返回
        # MsgPage(init_driver['driver']).newspage_understand()
        # assert MsgPage(init_driver['driver']).newspage_understand_assert()
        # BaseAction(init_driver['driver']).back()
        # 点击清空按钮 点击取消
        MsgPage(init_driver['driver']).newspage_clear()
        assert MsgPage(init_driver['driver']).newspage_clear_assert()
        MsgPage(init_driver['driver']).newspage_clear_no()
        # 点击清空按钮 点击确认
        MsgPage(init_driver['driver']).newspage_clear()
        MsgPage(init_driver['driver']).newspage_clear_yes()
        # 返回消息页
        BaseAction(init_driver['driver']).back()
        logger.info("互动消息页面case结束")
    # @allure.title("进入互动消息页面")
    # @allure.step("1、点击用户头像"
    #              "2、点击返回页面"
    #              "3、点击互动消息第一条消息"
    #              "4、点击返回页面"
    #              "5、点击清空按钮"
    #              "6、点击取消"
    #              "7、点击清空按钮"
    #              "8、点击确认"
    #              "9、返回消息页面")

    def test_CuteU_team(self,init_driver):
        logger.info("CuteU团队case开始")
        #点击消息-点击CuteU团队按钮 然后点击返回
        MsgPage(init_driver['driver']).CuteUTeam_jump()
        assert MsgPage(init_driver['driver']).CuteUTeam_jump_assert()
        BaseAction(init_driver['driver']).back()
        logger.info("CuteU团队case结束")
    # @allure.title("进入CuteU团队页面")
    # @allure.step("1、进入CuteU团队页面"
    #              "2、返回消息页面")

    def test_CuteU_Msg_VIP(self, init_driver):
        logger.info("用户主播聊天case开始")
        # 点击消息-点击消息页面第一个用户
        MsgPage(init_driver['driver']).CuteU_user()
        assert MsgPage(init_driver['driver']).CuteU_user_assert()

    # def test_user_page(self,init_driver):
    #     # 查看他的资料页
    #     MsgPage(init_driver['driver']).user_page()
    #     assert MsgPage(init_driver['driver']).user_page_assert()
    #     BaseAction(init_driver['driver']).back()

    '''是会员有钻石的情况下'''
    def test_user_msg(self,init_driver):
        # 发送消息
        MsgPage(init_driver['driver']).user_msg()
        MsgPage(init_driver['driver']).user_send()

    def test_user_voice(self,init_driver):
        # 发送语音消息
        MsgPage(init_driver['driver']).user_voice()
        assert MsgPage(init_driver['driver']).user_voice_assert()
        MsgPage(init_driver['driver']).voice_send()

    def test_user_img(self,init_driver):
        # 点击选择图片
        MsgPage(init_driver['driver']).user_img()
        assert MsgPage(init_driver['driver']).user_img_assert()
        MsgPage(init_driver['driver']).user_img_choose()
        assert MsgPage(init_driver['driver']).user_photo_assert()
        #点击小秘密按钮
        MsgPage(init_driver['driver']).user_secret()
        MsgPage(init_driver['driver']).user_secret()
        #发送图片
        MsgPage(init_driver['driver']).img_send()

    def test_user_video(self,init_driver):
        #点击视频聊天
        MsgPage(init_driver['driver']).user_video()
        assert MsgPage(init_driver['driver']).user_video_assert()
        MsgPage(init_driver['driver']).video_cancel()

    def test_user_call(self,init_driver):
        #点击语音聊天
        MsgPage(init_driver['driver']).user_call()
        assert MsgPage(init_driver['driver']).user_call_assert()
        MsgPage(init_driver['driver']).call_cancel()

    def test_user_gift(self,init_driver):
        #礼物按钮
        MsgPage(init_driver['driver']).user_gift()
        MsgPage(init_driver['driver']).gift_choose()
        MsgPage(init_driver['driver']).gift_send()
        assert MsgPage(init_driver['driver']).user_gift_assert()

    def test_user_red(self,init_driver):
        #点击红包按钮
        MsgPage(init_driver['driver']).user_red()
        assert MsgPage(init_driver['driver']).user_red_assert()
        MsgPage(init_driver['driver']).red_custom()
        MsgPage(init_driver['driver']).red_input()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).red_upload()
        MsgPage(init_driver['driver']).red_recharge()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).red_send()
        # BaseAction(init_driver['driver']).back()

    def test_user_more(self, init_driver):
        # 点击右上角三个点
        MsgPage(init_driver['driver']).user_more()
        assert MsgPage(init_driver['driver']).user_more_assert()
        # 点击用户头像
        MsgPage(init_driver['driver']).msg_more_user()
        BaseAction(init_driver['driver']).back()
        # 屏蔽按钮
        MsgPage(init_driver['driver']).msg_more_block()
        MsgPage(init_driver['driver']).msg_more_block()
        # 自动翻译按钮
        MsgPage(init_driver['driver']).msg_more_translate()
        MsgPage(init_driver['driver']).msg_more_translate()
        # 举报流程
        MsgPage(init_driver['driver']).msg_more_report()
        assert MsgPage(init_driver['driver']).msg_more_report_assert()
        MsgPage(init_driver['driver']).report_photo()
        MsgPage(init_driver['driver']).report_choose()
        MsgPage(init_driver['driver']).report_msg()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).report_submit()
        MsgPage(init_driver['driver']).report_ok()
        BaseAction(init_driver['driver']).back()
        BaseAction(init_driver['driver']).back()
        logger.info("用户与主播聊天case结束")
        # @allure.title("进入CuteU团队页面")
        # @allure.step("1、进入CuteU团队页面"
        #              "2、返回消息页面")

    def test_help_name(self,init_driver):
        logger.info("帮助中心case开始")
        MsgPage(init_driver['driver']).CuteU_help()
        BaseAction(init_driver['driver']).back()
        assert MsgPage(init_driver['driver']).CuteU_help_assert()
        logger.info("帮助中心case结束")

    def test_CuteU_help(self,init_driver):
        logger.info("消息页面右上角更多case开始")
        #点击消息-点击右上角更多按钮
        MsgPage(init_driver['driver']).CuteU_more()
        assert MsgPage(init_driver['driver']).CuteU_more_assert()
        #点击全部已读按钮
        MsgPage(init_driver["driver"]).read_all()
        #点击清理聊天列表
        MsgPage(init_driver['driver']).CuteU_more()
        MsgPage(init_driver["driver"]).more_clear()
        assert MsgPage(init_driver['driver']).more_clear_assert()
        MsgPage(init_driver["driver"]).more_cancel()
        MsgPage(init_driver['driver']).CuteU_more()
        MsgPage(init_driver["driver"]).more_clear()
        MsgPage(init_driver["driver"]).more_save()
    # @allure.title("点击右上角更多按钮")
    # @allure.step("1、全部已读按钮"
    #              "2、清理聊天列表"
    #              "3、取消清理聊天列表"
    #              "4、清理聊天列表"
    #              "5、确认清理聊天列表")

if __name__ == '__main__':
    x=setdriver().runapp()
    w=Testmsg()


