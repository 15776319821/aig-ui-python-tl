# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
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
#@pytest.mark.usefixtures("init_drivera")
class Testrecommend:
    def test_discover(self, init_driver):
        logger.info("非会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        RecommendPage(init_driver['driver']).discover()
        # 非会员点击筛选
        assert RecommendPage(init_driver['driver']).discover_screen(2)
        logger.info("非会员点击筛选按钮case开始结束")

    def test_discover_vip(self, init_driver):
        logger.info("会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-发现
        RecommendPage(init_driver['driver']).discover()
        # 非会员点击筛选
        assert RecommendPage(init_driver['driver']).discover_screen_vip(2)
        logger.info("会员点击筛选按钮case开始结束")

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

    # 推荐页-发现tab-点击卡片进入profile页
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

    # # 推荐列表-切换国家-非VIP
    # def test_recommend_screen(self,init_driver):
    #     logger.info("非会员点击筛选按钮case开始")
    #     # 点击推荐按钮
    #     RecommendPage(init_driver['driver']).recommend()
    #     # 点击推荐-推荐tab
    #     RecommendPage(init_driver['driver']).recommend_tab()
    #     # 点击列表第二个国家
    #     RecommendPage(init_driver['driver']).recommend_country_tab()
    #     # 断言出现会员拦截弹窗
    #     RecommendPage(init_driver['driver']).vip_intercept()
    #     # 关闭会员拦截弹窗
    #     RecommendPage(init_driver['driver']).vip_intercept_close()
    #     # 关闭关闭筛选框
    #     RecommendPage(init_driver['driver']).discover_screen_close()
    #     logger.info("非会员点击筛选按钮case开始结束")

    # 推荐列表-切换国家_vip
    def test_recommend_screen_vip(self,init_driver):
        logger.info("会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击列表第二个国家
        RecommendPage(init_driver['driver']).recommend_country_tab()


    def test_recommend_profile(self,init_driver):
        logger.info("点击推荐列表第一个主播")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击推荐列表第一个主播
        RecommendPage(init_driver['driver']).recommend_list(type=1)
        # profile用户昵称元素是否存在
        assert RecommendPage(init_driver['driver']).profile_name()
        RecommendPage(init_driver['driver']).profileReturnBtn()


if __name__ == '__main__':
    from base.base_driver import setdriver
    x=setdriver().runapp()
    w=Testrecommend()
    w.test_msg(init_driver=x)