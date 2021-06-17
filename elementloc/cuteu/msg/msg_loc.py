from selenium.webdriver.common.by import By

class MsgLoc():

    '''导航栏消息按钮'''
    msg_loc = (By.ID,"com.cuteu.videochat:id/btnTabMessage")     #导航栏消息按钮

    ''' 互动消息及互动消息内元素 '''
    interact_news = (By.ID,"com.cuteu.videochat:id/layout_im") #互动消息按钮
    news_clear = (By.ID,"com.cuteu.videochat:id/tv_right") #互动按钮内的清空按钮
    news_clear_yes =(By.ID,"android:id/button1") #确认清空
    news_clear_no = (By.ID,"android:id/button2") #取消清空
    news_head = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.ImageView[2]") #用户头像
    news_understand = (By.ID,"com.cuteu.videochat:id/tvMessage") #想了解XXX文字

    ''' CuteU团队信按钮 '''
    CuteU_team = (By.ID,"com.cuteu.videochat:id/layout_cs") #CuteU团队按钮

    ''' 客服中心及客服中心内元素'''
    CuteU_help = (By.ID,"com.cuteu.videochat:id/ivHelp") #客服中心按钮

    ''' 消息页面内更多及更多内按钮 '''
    CuteU_more = (By.ID,"com.cuteu.videochat:id/btnEdit") #更多按钮
    more_allread = (By.ID,"com.cuteu.videochat:id/btnAllRead") #全部已读按钮
    more_clear = (By.ID,"com.cuteu.videochat:id/btnDelete3Info") #清理聊天列表
    more_cancel = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[2]") #取消按钮
    more_save = (By.ID,"com.cuteu.videochat:id/tvSave")#确认按钮

    ''' 聊天页面及聊天页面内元素 '''
    msg_user = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.widget.LinearLayout[2]/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]")
    #列表中第一个用户
    user_page = (By.ID,"com.cuteu.videochat:id/checkTV") #查看他的资料页
    user_voice = (By.ID,"com.cuteu.videochat:id/btnChangeInputType") #麦克风按钮
    voice_send =(By.ID,"com.cuteu.videochat:id/btnPressSay")#点击按住说话
    user_msg = (By.ID,"com.cuteu.videochat:id/etInputText") #聊天框
    user_send = (By.ID,"com.cuteu.videochat:id/button") #发送按钮
    user_img = (By.ID,"com.cuteu.videochat:id/btnToSelectedImage") #图片按钮
    # 设为小秘密
    user_secret = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup")
    # 图片发送
    img_send = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[2]")
    user_video = (By.ID,"com.cuteu.videochat:id/btnToPhoneCell") #视频聊天
    user_call = (By.ID,"com.cuteu.videochat:id/btnToPhoneCellAudioOnly") #语音聊天
    user_red = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[4]") #红包按钮
    user_gift = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.ImageView[5]") #礼物按钮
    user_more = (By.ID,"com.cuteu.videochat:id/btnMoreInfo") #更多
    user_photo = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout/android.widget.ImageView")
    video_cancel = (By.ID,"com.cuteu.videochat:id/btnHangup") #发起视频后挂断
    call_cancel = (By.ID,"com.cuteu.videochat:id/btnHangup") #发起语音后挂断

    red_custom = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.view.View")
    #定制内容礼物选择
    red_input = (By.ID,"com.cuteu.videochat:id/etInput") #视频红包输入内容
    red_upload = (By.ID,"com.cuteu.videochat:id/cbOnlyRecord") #不允许本地上传
    red_recharge = (By.ID,"com.cuteu.videochat:id/btnRecharge") #充值
    red_send = (By.ID,"com.cuteu.videochat:id/tvConfirm") #发送

    gift_choose = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[4]/android.view.View[1]")
    #选择礼物
    gift_send = (By.ID,"com.cuteu.videochat:id/tvSendGift") #礼物发送

    msg_more_user = (By.ID,"com.cuteu.videochat:id/btnUserInfo") #点击用户
    msg_more_block = (By.ID,"com.cuteu.videochat:id/btnChangeBlockStatus") #屏蔽
    msg_more_translate = (By.ID,"com.cuteu.videochat:id/btnChangeTransLateStatus") #自动翻译
    msg_more_follow = (By.ID,"com.cuteu.videochat:id/btnFollow") #关注
    msg_more_report = (By.ID,"com.cuteu.videochat:id/btnReport") #举报
    report_photo = (By.ID,"com.cuteu.videochat:id/sdvShot") #上传截图
    #选择截图
    report_choose = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[2]/android.widget.ImageView")
    report_msg = (By.ID,"com.cuteu.videochat:id/etInput") #举报描述
    report_submit = (By.ID,"com.cuteu.videochat:id/btnSend") #提交举报
    report_ok = (By.ID,"com.cuteu.videochat:id/tvOK")#点击知道了按钮

    close_vip = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView")#关闭VIP弹窗
    #返回按钮
    return_page = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageButton")
   #个人主页返回按钮
    user_return_page = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.ImageView")

    #钻石弹窗拦截
    no_damond = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.view.ViewGroup/android.widget.TextView")

    #会员弹窗拦截
    no_vip = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.TextView[2]")

    #帮助中心
    help_name = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[1]/android.view.View/android.widget.TextView")
    #CuteU团队断言
    CuteU_team_assert = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/android.widget.TextView")
    #查看主播资料页断言
    user_page_assert = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.ImageView[2]")
    #钻石弹窗拦截
    close_diamond = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]")
    #送礼物钻石弹窗拦截
    gift_diamond_close = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]")
    #互动消息_用户消息_断言
    newspage_understand_assert = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]")