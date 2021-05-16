from base.base_log import logger
from pageproject.FancyMe.im_page import Im
import time
import pytest
class TestIm():

    def test_clickImPage(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
    def test_clickImPageFried(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(3)
        driver.handleException()
        driver.clickImPage()
        driver.clickFriend()
        driver.returnBtn()
    def test_clickImPageManageList(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.clickImManageList()
        driver.closeClickImManageList()
        driver.returnBtn()



