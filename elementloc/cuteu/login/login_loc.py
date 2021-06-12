# -*- coding:utf-8 -*-
# @Time     :2021/4/22 21:23
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :login_loc.py
# @Software :PyCharm

from selenium.webdriver.common.by import By

class LoginLoc():
    '''刚刚安装app时弹出的权限'''
    #首次安装时-授权许可
    submit_loc = (By.ID,"com.cuteu.videochat:id/tvSubmit")
    #定位始终允许
    location_allow_loc = (By.ID,"com.android.packageinstaller:id/permission_allow_button")
    #存储始终允许
    memory_allow_loc = (By.ID,"com.android.packageinstaller:id/permission_allow_button")

    '''选择注册或者登录方式的定位'''
    #快速注册
    fast_register_loc = (By.ID,"com.cuteu.videochat:id/tv_fast_register" )
    #谷歌登录
    google_login_loc = (By.ID,"com.cuteu.videochat:id/tvGoogleLogin")
    #选择需要登录的谷歌账号
    select_google_loc = (By.ID,"com.google.android.gms:id/account_display_name")
    #facebook登录
    facebook_longin_loc = (By.ID,"com.cuteu.videochat:id/tv_facebook")
    #选择需要登录的facebook账号
    select_facebook_loc = (By.XPATH,"//*[@text='继续']")
    #手机号登录
    mobile_phone_loc = (By.ID,"com.cuteu.videochat:id/tv_mobile_phone")
    #手机号输入框
    input_phone_loc = (By.ID,"com.cuteu.videochat:id/etMobilePhone")
    #发送验证码
    send_number_loc = (By.ID,"com.cuteu.videochat:id/tvGetVerifyCode")
    #输入验证码
    input_number_loc = (By.ID,"com.cuteu.videochat:id/etGetVerifyCode")
    #点击下一步，完成手机号登录
    phone_next_loc = (By.ID,"com.cuteu.videochat:id/tvNext")
    #快速注册以后选择其它登录方式后绑定账号
    confirm_loc = (By.ID, "android:id/button1")

    '''下面是注册时填写个人信息流程需要用到的元素'''
    #性别
    # 男
    male_loc = (By.ID,"com.cuteu.videochat:id/maleTv")
    #女
    female_loc = (By.ID,"com.cuteu.videochat:id/femaleTv")
    #性别-下一步
    gender_next_loc = (By.ID,"com.cuteu.videochat:id/next")

    #昵称
    #昵称-下一步
    nickname_next_loc = (By.ID,"com.cuteu.videochat:id/next")

    #生日
    #生日-下一步
    birthday_next_loc = (By.ID,"com.cuteu.videochat:id/next")

    #上传头像
    #上传头像-下一步
    photo_next_loc = (By.ID,"com.cuteu.videochat:id/next")

    #交友目的
    #交友目的-下一步
    purpose_next_loc = (By.ID,"com.cuteu.videochat:id/next")

    #获取权限
    #录音权限
    recording_loc = (By.ID,"com.android.packageinstaller:id/permission_allow_button")
    #摄像头权限
    camera_loc = (By.ID,"com.android.packageinstaller:id/permission_allow_button")
    #最后一步-我知道了
    iknow_loc = (By.ID,"com.cuteu.videochat:id/okBtn")






