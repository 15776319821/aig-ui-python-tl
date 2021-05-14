from pageproject.match_page import MatchPage
from base.base_log import logger
from pageproject.FancyMe.im_page import Im

class TestIm():
    def test_clickImPage(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        driver.clickImPage()
        driver.click1v1Message()
        driver.returnBtn()


