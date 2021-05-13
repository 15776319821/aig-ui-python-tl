# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import time

sys.path.append(os.getcwd())
from pageproject.cuteu.recommend.discover_page import DiscoverPage
from base.base_log import logger


# @pytest.fixture(scope='class')
# def init_driver():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.quit()
#@pytest.mark.usefixtures("init_drivera")
class Testmatch:
    def test_msg(self,init_driver):
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
        logger.info("非会员点击筛选按钮case开始结束")

if __name__ == '__main__':
    from base.base_driver import setdriver
    x=setdriver().runapp()
    w=Testmatch()
    w.test_msg(init_driver=x)