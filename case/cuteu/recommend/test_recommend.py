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
    # 推荐列表-点击banner
    def test_recommend_banner(self,init_driver):
        logger.info("推荐列表点击banner")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击推荐-推荐-banner
        RecommendPage(init_driver['driver']).recommend_banner()
    # 推荐列表-切换国家
    def test_recommend_screen(self,init_driver):
        logger.info("非会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击列表第二个国家
        RecommendPage(init_driver['driver']).recommend_country_tab()
        # 断言出现会员拦截弹窗
        RecommendPage(init_driver['driver']).vip_intercept()
        # 关闭会员拦截弹窗
        RecommendPage(init_driver['driver']).vip_intercept_close()
        # 关闭关闭筛选框
        RecommendPage(init_driver['driver']).discover_screen_close()
        logger.info("非会员点击筛选按钮case开始结束")

    def test_recommend_profile(self,init_driver):
        logger.info("非会员点击筛选按钮case开始")
        # 点击推荐按钮
        RecommendPage(init_driver['driver']).recommend()
        # 点击推荐-推荐tab
        RecommendPage(init_driver['driver']).recommend_tab()
        # 点击推荐列表第一个主播
        RecommendPage(init_driver['driver']).recommend_list(1)
        # profile用户昵称元素是否存在
        RecommendPage(init_driver['driver']).profile_name()




if __name__ == '__main__':
    from base.base_driver import setdriver
    x=setdriver().runapp()
    w=Testrecommend()
    w.test_msg(init_driver=x)