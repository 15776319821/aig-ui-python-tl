# -*- coding:utf-8 -*-

import os
import sys

sys.path.append(os.getcwd())
import time
from elementloc.cuteu.recommend.recommend_loc import ElementLoc
from base.base_action import BaseAction

class DiscoverPage(BaseAction):
    #
    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    def recommend(self):
        #q=self.driver.find_elemen
        # t(By.ID,'com.cuteu.videochat:id/btnTabMessage')
        #self.find_element(ElementLoc.match_loc1).click()
        self.click_element(ElementLoc.recommend_loc,"点击推荐")
        # print("页面级方法1")
        time.sleep(3)
    def discover(self):
        self.click_element(ElementLoc.discover_loc, '点击推荐-发现按钮')

    def discover_screen(self):
        self.click_element(ElementLoc.discover_screen_loc, '点击推荐-发现-筛选国家按钮')

    def discover_screen_list(self, type):
        self.click_elements(ElementLoc.discover_screen_list_loc, type, "点击第{}个国家".format(type))

    def discover_screen_close(self):
        self.click_element(ElementLoc.discover_screen_close_loc, '点击推荐-发现-筛选国家按钮关闭按钮')

    def discover_screen_card(self):
        self.click_element(ElementLoc.discover_screen_card_loc, '点击推荐-发现-卡片')

    def discover_swipeToLeft(self):
        self.swipeToLeft(start_x=0.2,end_x=0.9)

    def discover_swipeToRight(self):
        self.swipeToRight(start_x=0.2,end_x=0.9)

    def discover_screen_right_card(self):
        self.click_element(ElementLoc.discover_screen_card_loc, '右滑-卡片')

    def discover_screen_call(self):
        self.click_element(ElementLoc.discover_screen_call_loc, '点击推荐-发现-通话按钮')

    def vip_intercept(self):
        self.find_element(ElementLoc.vip_intercept_loc)

    def vip_intercept_close(self):
        self.click_element(ElementLoc.vip_intercept_close_loc, '点击关闭会员拦截弹窗')
