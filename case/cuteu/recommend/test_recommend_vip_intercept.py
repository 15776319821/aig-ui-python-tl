# -*- coding:utf-8 -*-
# 引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import time

sys.path.append(os.getcwd())
from pageproject.cuteu.recommend.recommend_page import RecommendPage
from base.base_log import logger
from base.base_action import BaseAction


# @pytest.fixture(scope='class')
# def init_driver():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.quit()
# @pytest.mark.usefixtures("init_drivera")
class Testrecommend():
    # 推荐列表切换国家—非VIP
    def test_discover(self, init_driver):
        logger.info("非会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        RecommendPage(init_driver['driver']).discover()
        # 非会员点击筛选
        assert RecommendPage(init_driver['driver']).discover_screen(2)
        logger.info("非会员点击筛选按钮case开始结束")


    # 推荐列表-切换国家-非VIP
    def test_recommend_screen(self, init_driver):
        logger.info("非会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击列表第二个国家
        RecommendPage(init_driver['driver']).recommend_country_tab()
        # 断言出现会员拦截弹窗
        assert RecommendPage(init_driver['driver']).vip_intercept()
        # 关闭关闭筛选框
        RecommendPage(init_driver['driver']).discover_screen_close()
        logger.info("非会员点击筛选按钮case开始结束")


if __name__ == '__main__':
    from base.base_driver import setdriver

    x = setdriver().runapp()
    w = Testrecommend()
