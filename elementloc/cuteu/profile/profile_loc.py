# -*- coding:utf-8 -*-
# @Time     :2021/5/27 15:23
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :profile_loc.py
# @Software :PyCharm
from selenium.webdriver.common.by import By

class ProfileLoc():
    #关注和取消关注元素
    heart_loc = (By.ID,"com.cuteu.videochat:id/heartFl")
    #个人语音介绍元素
    voice_loc = (By.ID,"com.cuteu.videochat:id/voice_bg")
    #切换teb到信息
    information_loc = (By.ID,"com.cuteu.videochat:id/information_title")
    #切换到tab Show
    show_loc = (By.ID,"com.cuteu.videochat:id/show_title")
    #切换查看照片
    photo_loc = (By.ID,"com.cuteu.videochat:id/photo_img")
    #私照的锁标识
    icon_loc = (By.ID,"com.cuteu.videochat:id/unLockView")
    #返回按键
    back_loc = (By.ID,"com.cuteu.videochat:id/topBackView")
    #Show视频·
    show_video = (By.ID,"com.cuteu.videochat:id/ivHead")
    #邀请完善资料
    invite_loc = (By.ID,"com.cuteu.videochat:id/notMore")
    #邀请完善身高
    height_loc = (By.XPATH,"//android.widget.CheckBox[@text='身高']")
    #邀请确定
    sure_loc = (By.ID,"com.cuteu.videochat:id/btnInvitation")
    #语音邀请
    phone_loc = (By.ID,"com.cuteu.videochat:id/imgVoiceChat")
    #语音挂断
    phone_end = (By.ID,"com.cuteu.videochat:id/btnHangup")
    #视频邀请
    call_video_loc = (By.ID,"com.cuteu.videochat:id/call_video")
    #视频挂断
    call_video_end = (By.ID,"com.cuteu.videochat:id/btnHangup")
    #请求录音权限
    recording_loc = (By.ID,"com.android.packageinstaller:id/permission_allow_button")
    #请求摄像头权限
    camera_loc = (By.ID,"com.android.packageinstaller:id/permission_allow_button")

