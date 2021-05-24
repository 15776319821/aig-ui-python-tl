# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import time
sys.path.append(os.getcwd())
from pageproject.cuteu.recommend.recommend_page import DiscoverPage
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
        DiscoverPage(init_driver['driver']).re
        # 点击推荐-发现-筛选



if __name__ == '__main__':
    from base.base_driver import setdriver
    x=setdriver().runapp()
    w=Testrecommend()
    w.test_msg(init_driver=x)