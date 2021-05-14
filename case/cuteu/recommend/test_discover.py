# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import time
sys.path.append(os.getcwd())
from pageproject.cuteu.recommend.discover_page import DiscoverPage
from base.base_log import logger
from base.base_action import BaseAction


# @pytest.fixture(scope='class')
# def init_driver():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.quit()
#@pytest.mark.usefixtures("init_drivera")
class Testrecommend:
    def test_discover(self,init_driver):
        logger.info("非会员点击筛选按钮case开始")
        # 点击推荐按钮
        DiscoverPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        DiscoverPage(init_driver['driver']).discover()
        # 点击推荐-发现-筛选
        DiscoverPage(init_driver['driver']).discover_screen()
        # 点击推荐-发现-筛选list第一个国际
        DiscoverPage(init_driver['driver']).discover_screen_list(1)
        # 断言出现会员拦截弹窗
        DiscoverPage(init_driver['driver']).vip_intercept()
        # 关闭会员拦截弹窗
        DiscoverPage(init_driver['driver']).vip_intercept_close()
        # 关闭关闭筛选框
        DiscoverPage(init_driver['driver']).discover_screen_close()
        logger.info("非会员点击筛选按钮case开始结束")

        # 推荐页-发现tab-滑动开卡片
    def test_sliding(self, init_driver):
        logger.info("滑动discover卡片case开始")
        # 点击推荐按钮
        DiscoverPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        DiscoverPage(init_driver['driver']).discover()
        # 点击推荐-发现-左滑卡片
        DiscoverPage(init_driver['driver']).swipeToLeft()
        # 点击推荐-发现-右滑卡片
        DiscoverPage(init_driver['driver']).swipeToRight()


    # 推荐页-发现tab-点击卡片进入profile页
    def test_profile(self,init_driver):
        logger.info("discover点击卡片进入profile页case开始")
        # 点击推荐按钮
        DiscoverPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        DiscoverPage(init_driver['driver']).discover()
        # 点击推荐-发现-点击卡片
        DiscoverPage(init_driver['driver']).discover_screen_card()


if __name__ == '__main__':
    from base.base_driver import setdriver
    x=setdriver().runapp()
    w=Testrecommend()
    w.test_msg(init_driver=x)