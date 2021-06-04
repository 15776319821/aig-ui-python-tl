# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import time
sys.path.append(os.getcwd())
from pageproject.cuteu.recommend.recommend_page import RecommendPage
from base.base_log import logger
import allure
from base.base_action import BaseAction


# @pytest.fixture(scope='class')
# def init_driver():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.quit()
#@pytest.mark.usefixtures("init_drivera")
@allure.feature("进入推荐页")
class Testrecommend():
    @allure.feature("进入推荐页")
    @allure.story("测试")
    def test_discover_vip(self, init_driver):
        logger.info("会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        RecommendPage(init_driver['driver']).discover()
        # 关闭手机绑定提示弹窗
        RecommendPage(init_driver['driver']).phone_binding()
        # 新手引导
        RecommendPage(init_driver['driver']).discover_guide()
        # 非会员点击筛选
        assert RecommendPage(init_driver['driver']).discover_screen_vip(2)
        logger.info("会员点击筛选按钮case开始结束")

    @allure.feature("进入推荐页")
    @allure.story("测试")
    @allure.title("discover页会员点击筛选按钮")
    @allure.step("1、进入推荐页"
                 "2、点击discover按钮"
                 "3、点击筛选按钮")

        # 推荐页-发现tab-滑动开卡片
    def test_sliding(self, init_driver):
        logger.info("滑动discover卡片case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        RecommendPage(init_driver['driver']).discover()
        # 点击推荐-发现-左滑卡片
        RecommendPage(init_driver['driver']).discover_swipeToLeft()
        # 点击推荐-发现-右滑卡片
        RecommendPage(init_driver['driver']).discover_swipeToRight()
        logger.info("滑动discover卡片case结束")
    @allure.title("滑动discover卡片")
    @allure.step("1、进入推荐页"
                 "2、点击discover按钮"
                 "3、左滑卡片"
                 "4、右滑卡片")

    # 推荐页-discover-点击卡片进入profile页
    def test_profile(self, init_driver):
        logger.info("discover点击卡片进入profile页case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        RecommendPage(init_driver['driver']).discover()
        # 点击推荐-发现-点击卡片
        assert RecommendPage(init_driver['driver']).discover_screen_card()
        # 连续返回
        RecommendPage(init_driver['driver']).profileReturnBtn()
        logger.info("discover点击卡片进入profile页case结束")
    @allure.title("滑动discover点卡片进入profile页")
    @allure.step("1、进入推荐页"
                 "2、点击discover按钮"
                 "3、点击卡片"
                 "4、profile页返回")

    # 推荐列表-点击banner
    def test_recommend_banner(self,init_driver):
        logger.info("推荐列表查看banner是否存在case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 推荐-推荐-banner是否存在
        assert RecommendPage(init_driver['driver']).recommend_banner()
        logger.info("推荐列表查看banner是否存在case结束")
    @allure.title("推荐列表查看banner是否存在")
    @allure.step("1、进入推荐页"
                 "2、点击推荐按钮"
                 "3、判断banner是否存在")

    # 推荐列表-切换国家_vip
    def test_recommend_screen_vip(self,init_driver):
        logger.info("会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击列表第二个国家
        RecommendPage(init_driver['driver']).recommend_country_tab()
    @allure.title("会员点击筛选按钮")
    @allure.step("1、进入推荐页"
                 "2、点击discover按钮"
                 "3、左滑卡片"
                 "4、右滑卡片")

    def test_recommend_profile(self,init_driver):
        logger.info("点击推荐列表第一个主播case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击推荐列表第一个主播
        assert RecommendPage(init_driver['driver']).recommend_list(type=1)
        RecommendPage(init_driver['driver']).profileReturnBtn()
        logger.info("点击推荐列表第一个主播case结束")
    @allure.title("点击推荐列表第一个主播")
    @allure.step("1、进入推荐页"
                 "2、点击推荐按钮"
                 "3、点击列表第一个主播进入profile页"
                 "4、profile页返回")

    def test_nearby_list(self,init_driver):
        logger.info("点击推荐列表第一个主播case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).nearby_tab()
        # 点击推荐列表第一个主播
        assert RecommendPage(init_driver['driver']).nearby_list(type=1)
        RecommendPage(init_driver['driver']).profileReturnBtn()
        logger.info("点击推荐列表第一个主播case结束")



if __name__ == '__main__':
    from base.base_driver import setdriver
    x=setdriver().runapp()
    w=Testrecommend()