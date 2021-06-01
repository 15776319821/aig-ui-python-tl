# -*- coding:utf-8 -*-
# 引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import time

from base.base_action import BaseAction

sys.path.append(os.getcwd())
from pageproject.cuteu.message.msg_page import MsgPage
from base.base_log import logger



class Testmsg:
    def test_msg(self,init_driver):
        logger.info("进入消息页面，点击一级页面元素")
        #点击消息按钮
        MsgPage(init_driver['driver']).msg_jump()
        #点击消息-互动消息
        MsgPage(init_driver['driver']).news_jump()
        #判断元素是否存在
        #如果在的话
        # 点击互动通知用户头像 点击返回
        MsgPage(init_driver['driver']).newspage_head()
        BaseAction(init_driver['driver']).back()
        #点击互动通知第一条消息 点击返回
        MsgPage(init_driver['driver']).newspage_understand()
        BaseAction(init_driver['driver']).back()
        #点击清空按钮 点击取消
        MsgPage(init_driver['driver']).newspage_clear()
        MsgPage(init_driver['driver']).newspage_clear_no()
        #点击清空按钮 点击确认
        MsgPage(init_driver['driver']).newspage_clear()
        MsgPage(init_driver['driver']).newspage_clear_yes()
        #返回消息页
        BaseAction(init_driver['driver']).back()
    #如果不在的话


    def CuteU_team(self,init_driver):
        #点击消息-点击CuteU团队按钮
        MsgPage(init_driver['driver']).CuteUTeam_jump()
        BaseAction(init_driver['driver']).back()

    #判断是否有用户存在，如果有的话。。。如果没用的话。。。会员情况，非会员情况
    #非会员
    def CuteU_Msg_User(self,init_driver):
        #点击消息-点击消息页面第一个用户
        MsgPage(init_driver['driver']).CuteU_user()
        #查看他的资料页
        MsgPage(init_driver['driver']).user_page()
        BaseAction(init_driver['driver']).back()
        #发送消息
        MsgPage(init_driver['driver']).user_msg()
        MsgPage(init_driver['driver']).user_send()
        BaseAction(init_driver['driver']).back()
        # 发送语音消息
        MsgPage(init_driver['driver']).user_voice()
        BaseAction(init_driver['driver']).back()
        #点击图片
        MsgPage(init_driver['driver']).user_img()
        BaseAction(init_driver['driver']).back()
        #点击视频聊天
        MsgPage(init_driver['driver']).user_video()
        BaseAction(init_driver['driver']).back()
        #点击语音聊天
        MsgPage(init_driver['driver']).user_call()
        BaseAction(init_driver['driver']).back()
        #点击红包按钮
        MsgPage(init_driver['driver']).user_red()
        BaseAction(init_driver['driver']).back()
        #礼物按钮
        MsgPage(init_driver['driver']).user_gift()
        BaseAction(init_driver['driver']).back()

        #点击右上角三个点
        MsgPage(init_driver['driver']).user_more()
        #点击用户头像
        MsgPage(init_driver['driver']).msg_more_user()
        BaseAction(init_driver['driver']).back()
        #屏蔽按钮
        MsgPage(init_driver['driver']).msg_more_block()
        MsgPage(init_driver['driver']).msg_more_block()
        #自动翻译按钮
        MsgPage(init_driver['driver']).msg_more_translate()
        MsgPage(init_driver['driver']).msg_more_translate()
        #举报流程
        MsgPage(init_driver['driver']).msg_more_report()
        MsgPage(init_driver['driver']).report_photo()
        MsgPage(init_driver['driver']).report_choose()
        MsgPage(init_driver['driver']).report_msg()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).report_submit()
        MsgPage(init_driver['driver']).report_ok()
        BaseAction(init_driver['driver']).back()

        #会员用户

    def CuteU_Msg_VIP(self, init_driver):
        # 点击消息-点击消息页面第一个用户
        MsgPage(init_driver['driver']).CuteU_user()
        # 查看他的资料页
        MsgPage(init_driver['driver']).user_page()
        BaseAction(init_driver['driver']).back()

        # 发送消息
        MsgPage(init_driver['driver']).user_msg()
        MsgPage(init_driver['driver']).user_send()
        # 发送语音消息
        MsgPage(init_driver['driver']).user_voice()
        MsgPage(init_driver['driver']).voice_send()
        # 点击图片
        MsgPage(init_driver['driver']).user_img()
        MsgPage(init_driver['driver']).report_choose()
        MsgPage(init_driver['driver']).user_secret()
        MsgPage(init_driver['driver']).user_secret()
        MsgPage(init_driver['driver']).img_send()
        #点击视频聊天
        MsgPage(init_driver['driver']).user_video()
        MsgPage(init_driver['driver']).video_cancel()
        #点击语音聊天
        MsgPage(init_driver['driver']).user_call()
        MsgPage(init_driver['driver']).call_cancel()
        #礼物按钮
        MsgPage(init_driver['driver']).user_gift()
        MsgPage(init_driver['driver']).gift_choose()
        MsgPage(init_driver['driver']).gift_send()
        #点击红包按钮
        MsgPage(init_driver['driver']).user_red()
        MsgPage(init_driver['driver']).red_custom()
        MsgPage(init_driver['driver']).red_input()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).red_upload()
        MsgPage(init_driver['driver']).red_recharge()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).red_send()

        # 点击右上角三个点
        MsgPage(init_driver['driver']).user_more()
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
        MsgPage(init_driver['driver']).report_photo()
        MsgPage(init_driver['driver']).report_choose()
        MsgPage(init_driver['driver']).report_msg()
        BaseAction(init_driver['driver']).back()
        MsgPage(init_driver['driver']).report_submit()
        MsgPage(init_driver['driver']).report_ok()
        BaseAction(init_driver['driver']).back()

    def CuteU_help(self,init_driver):
        #点击消息-点击右上角更多按钮
        MsgPage(init_driver['driver']).CuteU_help()
        #点击全部已读按钮
        MsgPage(init_driver["driver"]).read_all()
        #点击清理聊天列表
        MsgPage(init_driver["driver"]).more_clear()
        MsgPage(init_driver["driver"]).more_cancel()
        MsgPage(init_driver["driver"]).more_clear()
        MsgPage(init_driver["driver"]).more_save()






