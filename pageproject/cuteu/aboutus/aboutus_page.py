# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.getcwd())
sys.setrecursionlimit(100000)
import time
from base.base_action import BaseAction
from elementloc.cuteu.aboutus.aboutus_loc import AboutUsLoc


class AboutUs(BaseAction):
    def __init__(self,driver):
        BaseAction.__init__(self,driver)

    #我的-设置-关于我们—关于我们
    def Us(self,n):
        self.click_element(AboutUsLoc.us_loc,"点击我的")
        self.click_element(AboutUsLoc.set_loc,"点击设置齿轮角标")
        self.click_element(AboutUsLoc.set_aboutloc,"点击设置页面的关于我们")
        time.sleep(2)
        self.continuous_click(AboutUsLoc.aboutus_loc,n)
        self.click_element(AboutUsLoc.aboutus_loc,"点击顶部的关于我们")
        self.click_element(AboutUsLoc.backset_loc, "点击返回")
        time.sleep(3)
        self.click_element(AboutUsLoc.backset_loc1, "返回到我的页面")
