from selenium.webdriver.common.by import By

class MineLoc():
    #我的页面
    Mine=(By.ID,'com.aiglamour.ancho:id/btnTabMine')
    #设置页面
    Mine_settingBtn=(By.ID,'com.aiglamour.ancho:id/iv_setting')
    #设置页面-修改密码
    Mine_setting_setPwdBtn = (By.ID,'com.aiglamour.ancho:id/settingPassword')
    #设置页面-语言设置
    Mine_setting_changeLanguageBtn = (By.ID,'com.aiglamour.ancho:id/ll_change_language')
    #设置页面-绑定手机
    Mine_setting_setBindPhoneBtn = (By.ID,'com.aiglamour.ancho:id/settingBindPhone')
    #设置页面-常用语设置
    Mine_setting_setPhraseBtn = (By.ID,'com.aiglamour.ancho:id/settingPhrase')
    #设置页面-当前版本
    Mine_setting_version = (By.ID,'com.aiglamour.ancho:id/tvVersion')
    #设置月面-关于我们
    Mine_setting_setOurBtn = (By.ID,'com.aiglamour.ancho:id/tvVersion')
    #设置页面-退出登录
    Mine_setting_quitBtn= (By.ID,'com.aiglamour.ancho:id/settingQuit')
    #设置页面-关于我们-彩蛋按钮
    Mine_setting_setOurPage_easterEgg = (By.ID,'com.aiglamour.ancho:id/searchHintView')
    #返回按钮
    Mine_backBtn=(By.CLASS_NAME, 'android.widget.ImageButton')
    #主模块个人信息按钮
    Mine_userInfoBtn = (By.ID,'com.aiglamour.ancho:id/iv_edit')
    #主播信息设置页面title
    Mine_userInfo_title = (By.ID,'com.aiglamour.ancho:id/toolbar_title')
    #主模块用户名称
    Mine_userName = (By.ID,'com.aiglamour.ancho:id/iv_nickName')
    #主模块好友列表数量
    Mine_frienNumBtn = (By.ID,'com.aiglamour.ancho:id/tv_friendNum')
    #主模块关注列表数量
    Mine_followNumBtn = (By.ID, 'com.aiglamour.ancho:id/tv_followNum')
    #主模块粉丝数量按钮
    Mine_fansNumBtn = (By.ID,'com.aiglamour.ancho:id/tv_fansNum')
    #主模块查看了我
    Mine_lookMe = (By.ID,'com.aiglamour.ancho:id/layout_visitor')
    #主页面积分钱包
    Mine_wallet = (By.ID,'com.aiglamour.ancho:id/layout_wallet')
    #主页面段位
    Mine_level = (By.ID,'com.aiglamour.ancho:id/layout_level')
    #主页面擅长语言
    Mine_language = (By.ID,'com.aiglamour.ancho:id/layout_language')
    #主页面头像认证
    Mine_authentic = (By.ID,'com.aiglamour.ancho:id/layout_verify')
    #主页面我的相册
    Mine_myPicture = (By.ID,'com.aiglamour.ancho:id/layout_album_title')
    #主页面相册数量
    Mine_pictureNum = (By.ID,'com.aiglamour.ancho:id/tv_album_num')
    #用户信息设置页面-用户昵称
    Mine_setUserInfo_userName= (By.ID,'com.aiglamour.ancho:id/tvUserName')
    #用户信息设置页面-用户出生日期
    Mine_setUserInfo_brith = (By.ID,'com.aiglamour.ancho:id/tvUserBirth')
    #用户信息设置页面-身高
    Mine_setUserInfo_userHeight = (By.ID,'com.aiglamour.ancho:id/tvUserHeight')
    #用户信息设置页面-体重
    Mine_setUserInfo_userWeight = (By.ID,'com.aiglamour.ancho:id/tvUserWeight')
    #用户信息设置页面-学历
    Mine_setUserInfo_userEducation = (By.ID,'com.aiglamour.ancho:id/tvUserEducation')
    #用户信息设置页面-职业
    Mine_setUserInfo_userJob = (By.ID,'com.aiglamour.ancho:id/tvUserProfession')
    #用户信息设置页面-自我介绍
    Mine_setUserInfo_userIntroduce = (By.ID,'com.aiglamour.ancho:id/editAutograph')
    #用户信息设置页面-我的兴趣
    Mine_setUserInfo_userInterest = (By.ID,'com.aiglamour.ancho:id/editInterest')

