# -*- coding:utf-8 -*-

from selenium.webdriver.common.by import By
#为了能打开app的截图彩蛋而找的元素
class AboutUsLoc():
    #一级tab—我的
    us_loc = (By.ID,"com.cuteu.videochat:id/btnTabMine")
    #右上角的设置
    set_loc = (By.ID,"com.cuteu.videochat:id/imgSet")
    #设置—关于我们'
    set_aboutloc = (By.XPATH,"//*[@text='关于我们']")
    #设置—关于我们—关于我们
    aboutus_loc = (By.ID,"com.cuteu.videochat:id/toolbar_title")
    #设置—关于我们—关于我们—返回
    backset_loc =(By.CLASS_NAME,"android.widget.ImageButton")
