# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())
import time
from elementloc.cuteu.match.match_loc import ElementLoc
from base.base_action import BaseAction

class MatchPage(BaseAction):
    #
    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    def match(self):
        #q=self.driver.find_elemen
        # t(By.ID,'com.cuteu.videochat:id/btnTabMessage')
        #self.find_element(ElementLoc.match_loc1).click()
        self.click_element(ElementLoc.matchCity,"点击匹配按钮")
        #print("页面级方法1")
        time.sleep(3)

    def msglist(self,c):
        self.click_elements(ElementLoc.maglist_loc,c,"点击第{}个元素".format(c))

    def match_history(self):

        self.click_element(ElementLoc.match_history, "点击匹配历史记录icon")

    def match_pairing(self):
        self.click_element(ElementLoc.match_pairing,'点击配对列表')

    def match_pairingid(self):
        return self.is_exist(ElementLoc.match_pairingid)

    def match_return(self):
        self.click_element(ElementLoc.match_return,'点击返回')

    def match_saihi(self):
        return self.is_exist(ElementLoc.match_saihi)

    def match_carousel(self):
        self.click_element(ElementLoc.match_carousel,'点击轮播图跳转个人空间页')

    def match_video(self):
        return self.is_exist(ElementLoc.match_video)

    def match_carouselid(self):
        self.click_element(ElementLoc.match_carouselid,'点击轮播图跳转个人空间页')

    def match_carouselreturn(self):
        self.click_element(ElementLoc.match_carouselreturn,'点击返回')

    def match_quickmatch(self):
        self.click_element(ElementLoc.match_quickmatch,'点击快速匹配')

    def match_matchongoing(self):
        return self.is_exist(ElementLoc.match_ongoing)

    def match_matchclose(self):
        self.click_element(ElementLoc.match_close,'关闭匹配功能')

    def match_closeView(self):
        self.click_element(ElementLoc.match_closeView,'关闭页面')

    def match_nextmatch(self):
        self.click_element(ElementLoc.match_nexting,'点击匹配下一个')

    def match_success(self):
        return self.is_exist(ElementLoc.match_success)