# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())
import time
from elementloc.cuteu.match_loc import ElementLoc
from base.base_action import BaseAction

class MatchPage(BaseAction):
    #
    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    def match(self):
        #q=self.driver.find_elemen
        # t(By.ID,'com.cuteu.videochat:id/btnTabMessage')
        #self.find_element(ElementLoc.match_loc1).click()
        self.click_element(ElementLoc.match_loc1,"点击消息列表")
        print("页面级方法1")
        time.sleep(3)

    def msglist(self,c):
        self.click_elements(ElementLoc.maglist_loc,c,"点击第{}个元素".format(c))

    def msgteam(self):
        self.click_element(ElementLoc.msgteam_loc,"点击CuteU团队")
        self.click_element(ElementLoc.msgteam_return_loc, "团队信点击返回按钮")