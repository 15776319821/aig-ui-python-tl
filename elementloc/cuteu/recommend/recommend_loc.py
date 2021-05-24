from selenium.webdriver.common.by import By

class ElementLoc:

    #会员拦截弹窗
    vip_intercept_loc = (By.ID,"com.cuteu.videochat:id/tvTitle")
    #会员拦截弹窗关闭按钮
    vip_intercept_close_loc = (By.ID, 'com.cuteu.videochat:id/tvClose')

    #一级页面推荐按钮
    recommend_loc = (By.ID, 'com.cuteu.videochat:id/btnTabRecommend')
    #推荐页-发现按钮
    discover_loc = (By.XPATH, '//android.widget.LinearLayout[@content-desc="发现"]/android.view.ViewGroup/android.widget.TextView')
    #推荐页-发现-筛选按钮
    discover_screen_loc = (By.ID, 'com.cuteu.videochat:id/countryTv')
    #推荐页-发现-筛选list
    discover_screen_list_loc = (By.ID, 'com.cuteu.videochat:id/nameTv')
    #推荐页-发现-筛选关闭按钮
    discover_screen_close_loc = (By.ID, 'com.cuteu.videochat:id/closeBarView')
    #推荐页-发现-卡片
    discover_screen_card_loc = (By.ID, 'com.cuteu.videochat:id/bgView')
    # 推荐页-发现-通话按钮
    discover_screen_call_loc = (By.ID, 'com.cuteu.videochat:id/callView')

    # profile页昵称
    profile_name= (By.ID, 'com.cuteu.videochat:id/userName')

    # 推荐-推荐tab按钮
    recommended_tab_loc = (By.XPATH, '//android.widget.LinearLayout[@content-desc="推荐"]/android.view.ViewGroup/android.widget.TextView')
    # 推荐-更多按钮
    recommended_more_loc = (By.ID, 'com.cuteu.videochat:id/ivMore')
    # 推荐-国家tab第二个
    recommended_country_tab_loc = (By.ID, 'com.cuteu.videochat:id/tv_title_2')
    # 推荐-banner
    recommend_banner_loc = (By.ID, 'com.cuteu.videochat:id/bannerLayout')
    # 推荐-列表
    recommend_list_loc = (By.ID, 'com.cuteu.videochat:id/bgView')