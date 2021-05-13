from selenium.webdriver.common.by import By

class ImLoc():
    #消息模块
    Im_loc=(By.ID,'com.aiglamour.ancho:id/btnTabMessage')
    #团队按钮
    Im_team=(By.NAME,'FancyMe团队')
    #互动消息
    Im_notice=(By.NAME,'互动通知')
    #Im模块消息文字
    Im_imText=(By.XPATH,'//android.widget.LinearLayout[@content-desc="消息"]/android.view.ViewGroup/android.widget.TextView')
    #Im模块好友按钮
    Im_friedButton=(By.ID,'com.aiglamour.ancho:id/btnRelation')
    #Im模块消息统一处理按钮
    Im_news_manage_list=(By.ID,'com.aiglamour.ancho:id/btnEdit')
    #Im模块1v1消息最后时间
    Im_news_lastTime=(By.ID,'com.aiglamour.ancho:id/tvLastTime')
    #Im模块1v1消息用户剩余钻石
    Im_news_diamond=(By.ID,'com.aiglamour.ancho:id/tv_diamond')
    #1v1消息页面对方信息设置
    Im_news_1v1message_moreInfo=(By.ID,'com.aiglamour.ancho:id/btnMoreInfo')
    #1V1消息切换语音文字按钮
    Im_news_1v1message_changeInput=(By.ID,'com.aiglamour.ancho:id/btnChangeInputType')
    #1v1消息输入框
    Im_news_1v1message_inputText=(By.ID,'com.aiglamour.ancho:id/tvDiamond')
    #1v1语音消息按钮
    Im_news_1v1message_vioceBtn=(By.ID,'com.aiglamour.ancho:id/btnPressSay')
    #1v1消息预设置消息按钮
    Im_news_1v1message_btnReply=(By.ID,'com.aiglamour.ancho:id/btnReply')
    #1V1消息发送按钮
    Im_news_1v1message_sendBtn=(By.ID,'com.aiglamour.ancho:id/button')
    #1v1发送图片按钮
    Im_news_1v1messsage_sendPicBtn=(By.ID,'com.aiglamour.ancho:id/btnToSelectedImage')
    #1v1发送视频通话按钮
    Im_news_1v1messsage_sendVideoCall=(By.ID,'com.aiglamour.ancho:id/btnToPhoneCell')
    #1v1发送语音通话按钮
    Im_news_1v1messsage_sendVoiceCall=(By.ID,'com.aiglamour.ancho:id/btnToPhoneCellAudioOnly')
    #1v1发送私密图片按钮
    Im_news_1v1messsage_sendSecretBtn=(By.ID,'com.aiglamour.ancho:id/btnOpenSecret')
    #1v1礼物商城按钮
    Im_news_1v1messsage_openGiftBtn=(By.ID,'com.aiglamour.ancho:id/btnOpenGift')
    #1v1对方昵称
    Im_news_1v1messsage_nickName=(By.ID,'com.aiglamour.ancho:id/tvNickName')
    #1v1对方钻石数量
    Im_news_1v1messsage_diamond=(By.ID,'com.aiglamour.ancho:id/tvDiamond')
    #1v1消息页面返回按钮
    Im_news_1v1message_returnBtn=(By.CLASS_NAME,'android.widget.ImageButton')
    #1v1消息页面亲密度按钮
    Im_news_1v1message_relationBtn=(By.ID,'com.aiglamour.ancho:id/btnRelationShip')
    #1v1消息页面对方昵称
    Im_news_1v1message_nickName=(By.ID,'com.aiglamour.ancho:id/tvNickName')
    #1v1消息页面亲密度弹窗进度条
    Im_news_1v1message_heartRate=(By.ID,'com.aiglamour.ancho:id/seekBar')
    #1v1消息亲密度弹窗详情
    Im_news_1v1message_heartRateInfo=(By.ID,'com.aiglamour.ancho:id/pList')
    #1v1消息当前亲密度
    Im_news_1v1message_heartRateNum=(By.ID,'com.aiglamour.ancho:id/tvCurrentIntimacy')
    #1v1消息距离下一级需要亲密值
    Im_news_1v1message_nextHeartLevelNum=(By.ID,'com.aiglamour.ancho:id/tvCurrentIntimacy')
    #1v1消息-对方用户设置-用户信息页
    Im_news_1v1message_moreInfo_userInfoBtn=(By.ID,'com.aiglamour.ancho:id/btnUserInfo')
    # 1v1消息-对方用户设置-屏蔽按钮
    Im_news_1v1message_moreInfo_shieldBtn=(By.ID,'com.aiglamour.ancho: id / btnChangeBlockStatus')
    # 1v1消息-对方用户设置-自动翻译按钮
    Im_news_1v1message_moreInfo_translateBtn=(By.ID,'com.aiglamour.ancho:id/btnChangeTransLateStatus')
    # 1v1消息-对方用户设置-举报按钮
    Im_news_1v1message_moreInfo_reportBtn=(By.ID,'com.aiglamour.ancho:id/btnReport')
    # 1v1消息-对方用户设置-举报按钮
    Im_news_1v1message_moreInfo_followBtn=(By.ID,'com.aiglamour.ancho:id/btnFollow')
    #1v1消息亲密度不足弹窗
    Im_news_1v1message_heartRateLessAlert=(By.ID,'com.aiglamour.ancho:id/clParent')
    #1v1消息亲密度不足弹窗确认按钮
    Im_news_1v1message_heartRateLessAlertCloseBtn=(By.ID,'com.aiglamour.ancho:id/tvSubmit')

