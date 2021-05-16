from base.base_log import logger
from pageproject.FancyMe.im_page import Im
from base.base_action import BaseAction
import time
class TestIm():
    def test_clickImPage(self,init_driver):

        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(3)
        driver.handleException()
        driver.clickImPage()
        driver.clickFriend()
        driver.leftPage()


