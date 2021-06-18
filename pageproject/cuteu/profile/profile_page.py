# -*- coding:utf-8 -*-
# @Time     :2021/5/28 19:45
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :profile_page.py
# @Software :PyCharm

import os
import sys
sys.path.append(os.getcwd())
from elementloc.cuteu.profile.profile_loc import ProfileLoc
from base.base_action import BaseAction
from base.base_log import logger
from elementloc.cuteu.aboutus.aboutus_loc import AboutUsLoc
import time

class ProfilePage(BaseAction):
    '''通过搜索彩蛋进入个人空间页'''
    def into_profile(self):
        self.click_element(AboutUsLoc.us_loc,'进入我的页面')
        self.click_element(AboutUsLoc.set_loc,'设置')
        self.click_element(AboutUsLoc.set_aboutloc,'关于我们')
        time.sleep(2)
        self.continuous_click(self.find_element(AboutUsLoc.aboutus_loc),20)
        self.click_element(AboutUsLoc.backset_loc1,'返回')
        time.sleep(1)
        self.input_text(AboutUsLoc.uid_loc,10051549,'搜索对应主播')
        self.click_element(AboutUsLoc.inputuid_loc,'点击搜索')
        a = self.ele_text(ProfileLoc.username_loc)
        assert a =="秃头披风侠", '断言失败，没有跳转到个人空间页'
    '''这是个人空间页一级页面的所有步骤'''
    #点击爱心用以关注和取消
    def heart(self):
        self.click_element(ProfileLoc.heart_loc,'点击爱心关注或者取消关注')
    #点击个人语音介绍
    def voice(self):
        self.click_element(ProfileLoc.voice_loc,'点击播放个人语音')
    #点击下方的语音邀请--会员的情况
    def phone_vip(self):
        self.click_element(ProfileLoc.phone_loc,'邀请语音聊天')
        self.click_element(ProfileLoc.phone_end,'挂断语音聊天')
    #点击下方的语音邀请--非会员的情况
    def phone_novip(self):
        self.click_element(ProfileLoc.phone_loc, '邀请语音聊天')
        self.click_element(ProfileLoc.vip_close_loc, '这个账号还不是会员呢，没有办法进行语音邀请')
    '''
    #这是未作会员非会员处理的语音邀请
    def phone(self):
        self.click_element(ProfileLoc.phone_loc, '邀请语音聊天')
        a = self.is_elementloc(ProfileLoc.recording_loc)
        b = self.ele_text(ProfileLoc.vip_intercept_loc)
        if a:
            self.click_element(ProfileLoc.recording_loc, '允许录音权限开启')
        elif b == '成为会员':
            self.click_element(ProfileLoc.vip_close_loc, '这个账号还不是会员呢，没有办法进行语音邀请')
        else:
            self.click_element(ProfileLoc.phone_end, '挂断语音聊天')
    
    #这是未作会员非会员处理的视频邀请
    def call_video(self):
        self.click_element(ProfileLoc.call_video_loc,'邀请视频聊天')
        a = self.is_elementloc(ProfileLoc.camera_loc)
        b = self.ele_text(ProfileLoc.vip_intercept_loc)
        if a :
            self.click_element(ProfileLoc.camera_loc,'允许摄像头权限开启')
        elif b == "成为会员":
            self.click_element(ProfileLoc.vip_close_loc,'这个账号还不是会员，不能进行视频邀请')
        else:
            self.click_element(ProfileLoc.call_video_end,'挂断视频聊天')
    '''
    #点击下方的语音邀请--会员的情况
    def call_video_vip(self):
        self.click_element(ProfileLoc.call_video_loc,'邀请视频聊天')
        self.click_element(ProfileLoc.call_video_end,'挂断视频聊天')
    #点击下方的语音邀请 - -非会员的情况
    def call_video_novip(self):
        self.click_element(ProfileLoc.call_video_loc,'邀请视频聊天')
        self.click_element(ProfileLoc.vip_close_loc, '这个账号还不是会员，不能进行视频邀请')
    #查看照片
    def select_photo(self):
        self.click_elements(ProfileLoc.photo_loc,2,'查看第二张照片')
    # 左滑
    def profile_swipeToLeft(self):
        logger.info('左滑')
        self.swipeToLeft(0.2,0.9,y1=0.3)
    # 右滑
    def profile_swipeToRight(self):
        logger.info('右滑')
        self.swipeToRight(0.9,0.2)
    #上滑
    def profile_swipeToUP(self):
        self.swipeToUp(start_y=0.6,end_y=0.3)
    #下滑
    def profile_swipeToDown(self):
        time.sleep(2)
        self.swipeToDown(start_y=0.3,end_y=0.6)

    '''消息页签下的操作'''
    def switch_information(self):
        self.click_element(ProfileLoc.information_loc,'切换到消息tab页')
    def information_invite(self):
        time.sleep(2)
        self.click_element(ProfileLoc.invite_loc,'邀请完善资料')
        # d = self.ele_text(ProfileLoc.height_loc)
        # assert d == '身高' , '没有唤醒邀请完善资料页面'
        self.click_element(ProfileLoc.height_loc,'邀请完善身高')
        self.click_element(ProfileLoc.sure_loc,'确定')
        time.sleep(2)
        self.back()
        time.sleep(2)
        self.back()
    '''show页面下的操作'''
    def switch_show(self):
        self.click_element(ProfileLoc.show_loc,'切换到show tab页')
    def show_voice(self):
        c = self.ele_text(ProfileLoc.show_title_loc)
        assert c == '她收到的评价', '没有切换到show页面'
        self.click_element(ProfileLoc.show_video,'播放show视频')
        time.sleep(3)
        self.back()