# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os
import sys
import pytest
sys.path.append(os.getcwd())
from pageproject.cuteu.match.match_page import MatchPage
from base.base_log import logger
from pageproject.cuteu.login import login_page


# @pytest.fixture(scope='class')
# def init_driver():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.quit()
#@pytest.mark.usefixtures("init_drivera")
class Testmatch:
    #检查匹配记录配对页
    def test_pair(self,init_driver):
        logger.info("开始执行")
        #driver=init_driver['driver']
        #driver.find_element_by_id('com.cuteu.videochat:id/ivMatchHistory').click()
        #点击匹配模块
        MatchPage(init_driver['driver']).match()
        #点击匹配历史按钮
        MatchPage(init_driver['driver']).match_history()
        #点击配对列表
        MatchPage(init_driver['driver']).match_pairing()
        #断言元素是否存在
        assert MatchPage(init_driver['driver']).match_pairingid()
        #返回上一页
        MatchPage(init_driver['driver']).match_return()
        logger.info("执行结束")


    #检查匹配记录历史页
    def test_history(self,init_driver):
        logger.info("开始执行")
        #点击匹配历史按钮
        MatchPage(init_driver['driver']).match_history()
        #断言元素是否存在
        assert MatchPage(init_driver['driver']).match_saihi()
        #返回上一页
        MatchPage(init_driver['driver']).match_return()
        logger.info("执行结束")


    #点击轮播图跳转个人空间页
    def test_carousel(self, init_driver):
        logger.info("开始执行")
        #点击轮播图
        MatchPage(init_driver['driver']).match_carouselid()
        #断言元素是否存在
        assert MatchPage(init_driver['driver']).match_video()
        #返回上一页
        MatchPage(init_driver['driver']).match_carouselreturn()
        logger.info("执行结束")

    #匹配关闭功能
    def test_matchcloseed(self,init_driver):
        logger.info("开始执行")
        #点击匹配
        MatchPage(init_driver['driver']).match_quickmatch()
        #检查匹配进行中
        assert MatchPage(init_driver['driver']).match_matchongoing()
        #关闭匹配
        MatchPage(init_driver['driver']).match_matchclose()
        #关闭页面
        MatchPage(init_driver['driver']).match_closeView()
        logger.info("执行结束")

    #匹配下一个

    def test_nextmatch(self,init_driver):
        logger.info("开始执行")
        #点击匹配
        MatchPage(init_driver['driver']).match_quickmatch()
        #检查匹配进行中
        assert MatchPage(init_driver['driver']).match_matchongoing()
        #点击下一个匹配
        MatchPage(init_driver['driver']).match_nextmatch()
        #检查匹配进行中
        assert MatchPage(init_driver['driver']).match_matchongoing()
        #检查匹配成功
        assert MatchPage(init_driver['driver']).match_success()

        #MatchPage(init_driver['driver']).match_matchclose()
        #关闭页面
        MatchPage(init_driver['driver']).match_closeView()
        logger.info("执行结束")

