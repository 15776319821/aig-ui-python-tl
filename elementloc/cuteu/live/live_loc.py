from selenium.webdriver.common.by import By

class LiveLoc():

    live_loc = (By.ID, "com.cuteu.videochat:id/btnTabLive")  # 导航栏直播按钮

    top_live =  (By.NAME,"直播") #顶部导航栏直播
    top_follow = (By.NAME,"关注") #顶部导航栏关注

    user_live = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.LinearLayout")
    #第一个直播主播

    room_username = (By.ID,"com.cuteu.videochat:id/tvUsername") #主播名字
    room_damond = (By.ID,"com.cuteu.videochat:id/ll_diamond") #钻石按钮
    room_msg = (By.ID,"com.cuteu.videochat:id/showKeyBroad") #发送消息
    room_notice = (By.ID,"com.cuteu.videochat:id/ivNotice") #公告
    room_gift = (By.ID,"com.cuteu.videochat:id/ivNotice") #礼物
    room_exit = (By.ID,"com.cuteu.videochat:id/btnExit") #关闭直播间
    #点击贡献榜
    room_user = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup[2]/android.widget.ImageView[4]")
    room_sendgift = (By.ID,"com.cuteu.videochat:id/follow") #提示赠送礼物
    room_follow = (By.ID,"com.cuteu.videochat:id/btnFollow") #关注主播
    username_head = (By.ID,"com.cuteu.videochat:id/sdvAvatar")#点击主播头像
    username_report = (By.ID,"com.cuteu.videochat:id/sdvAvatar")#点击举报主播
    username_follow = (By.ID,"com.cuteu.videochat:id/sdvAvatar")#点击关注主播
    username_close = (By.ID,"com.cuteu.videochat:id/btnClose")#关闭主播信息

    room_gift_choose = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[8]/android.widget.ImageView[1]")
    #选择礼物
    room_gift_send = (By.ID,"com.cuteu.videochat:id/tvSendGift") #发送礼物
    room_gift_recharge = (By.ID,"com.cuteu.videochat:id/btn_recharge") #充值钻石