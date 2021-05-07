from selenium.webdriver.common.by import By

class ElementLoc:
    #一级页面消息按钮
    match_loc1 = (By.ID, 'com.cuteu.videochat:id/btnTabMessage')
    #消息列表
    maglist_loc = (By.ID, 'com.cuteu.videochat:id/linearLayout2')
    #团队信
    msgteam_loc = (By.ID, 'com.cuteu.videochat:id/layout_cs')
    #团队信返回按钮
    msgteam_return_loc = (By.CLASS_NAME, "android.widget.ImageButton")

