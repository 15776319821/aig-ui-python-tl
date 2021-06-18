# -*- coding:utf-8 -*-

import os
import sys
sys.path.append(os.getcwd())
import time
from elementloc.cuteu.recommend.recommend_loc import ElementLoc
from base.base_action import BaseAction
from base.base_log import logger

class RecommendPage(BaseAction):
    #
    # def __init__(self,driver):
    #     BaseAction.__init__(self,driver)
    def recommend(self):
        self.click_element(ElementLoc.recommend_loc, "点击推荐")
        # print("页面级方法1")

    def discover(self):
        self.click_element(ElementLoc.discover_loc, '点击推荐-发现按钮')

    # 非会员点击筛选
    def discover_screen(self, type):
        try:
            self.click_element(ElementLoc.discover_screen_loc, '点击推荐-发现-筛选国家按钮')
            self.discover_screen_list(type)
            if self.vip_intercept():
                self.discover_screen_close()
                return True
            else:
                return False
        except:
            logger.info("筛选弹窗异常")
            return False

    # 会员点击筛选
    def discover_screen_vip(self, type):
        try:
            self.click_element(ElementLoc.discover_screen_loc, '点击推荐-发现-筛选国家按钮')
            self.discover_screen_list(type)
            return True
        except:
            logger.info("筛选弹窗异常")
            return False

    def discover_screen_list(self, type):
        self.click_elements(ElementLoc.discover_screen_list_loc, type, "点击第{}个国家".format(type))

    def discover_screen_close(self):
        self.click_element(ElementLoc.discover_screen_close_loc, '点击推荐-发现-筛选国家按钮关闭按钮')

    def discover_screen_card(self):
        if self.is_exist(ElementLoc.discover_screen_card_loc)==True:
            self.click_element(ElementLoc.discover_screen_card_loc, '点击discover卡片')
            if self.profile_name():
                logger.info("进入profile页成功")
                return True
            else:
                logger.info("进入profile页失败")
                return False
        else:
            return False

    # 左滑
    def discover_swipeToLeft(self):
        self.swipeToLeft(start_x=0.2,end_x=0.9)

    # 右滑
    def discover_swipeToRight(self):
        self.swipeToRight(start_x=0.9,end_x=0.2)



    def discover_screen_call(self):
        self.click_element(ElementLoc.discover_screen_call_loc, '点击推荐-发现-通话按钮')

    # 出现会员拦截弹窗后关闭
    def vip_intercept(self):
        try:
            if "成为会员" == self.getElementText(ElementLoc.vip_intercept_loc):
                logger.info("出现会员拦截弹窗")
                self.find_element(ElementLoc.vip_intercept_loc)
                self.vip_intercept_close()
                logger.info("会员拦截弹窗以关闭")
                return True
            else:
                logger.info("无会员拦截弹窗")
                return False
        except:
            logger.info("未出现会员拦截弹窗")
            return False


    def vip_intercept_close(self):
        self.click_element(ElementLoc.vip_intercept_close_loc, '点击关闭会员拦截弹窗')

    # 查找profle页用户昵称元素
    def profile_name(self):
        return self.is_exist(ElementLoc.profile_name)

    def recommend_tab(self):
        self.click_element(ElementLoc.recommend_tab_loc, '点击推荐tab')

    def recommend_more(self):
        self.click_element(ElementLoc.recommend_more_loc, '点击推荐国家更多按钮')

    def recommend_country_tab(self):
        if self.is_exist(ElementLoc.recommend_country_tab_loc):
            self.click_element(ElementLoc.recommend_country_tab_loc, '点击国家tab第二个国家')
            return True
        else:
            return False

    def recommend_list(self, type):
        self.click_elements(ElementLoc.recommend_list_loc,type, '点击推荐列表的第{}个主播'.format(type))
        return self.is_exist(ElementLoc.recommend_nearby_list_loc)

    def recommend_banner(self):
        return self.is_exist(ElementLoc.recommend_banner_loc)

    def profileReturnBtn(self):
        if self.is_exist(ElementLoc.profile_returnBtn_loc):
            self.click_element(ElementLoc.profile_returnBtn_loc, '返回按钮')
            logger.info("点击profile页返回按钮")
            
    def nearby_tab(self):
        self.click_element(ElementLoc.recommend_nearby_loc, '点击同城tab')
            
    def nearby_list(self,type):
        if self.is_exist(ElementLoc.recommend_nearby_list_loc):
            self.click_elements(ElementLoc.recommend_nearby_list_loc, type, '点击推荐列表的第{}个主播'.format(type))
            return self.is_exist(ElementLoc.profile_name)
        else:
            return False

    def discover_guide(self):
        if self.is_exist(ElementLoc.discover_guide):
            self.click_element(ElementLoc.discover_guide, 'discover页点击新手引导')

    def phone_binding(self):
        if self.is_exist(ElementLoc.recommend_phone_binding):
            self.click_element(ElementLoc.recommend_cancel_binding, '点击绑定手机号取消按钮')


