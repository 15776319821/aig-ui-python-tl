from base.base_log import logger
from pageproject.FancyMe.im_page import Im
from pageproject.FancyMe.mine_page import Mine
from base.base_action import BaseAction
import time
class TestIm():
    # def test_clickImPage(self,init_driver):
    #     logger.info("开始进入Im模块")
    #     driver = Im(init_driver['driver'])
    #     time.sleep(5)
    #     driver.handleException()
    #     time.sleep(2)
    #     driver.clickIm()
    #     driver.click1v1Message(clickStatus=2)
    #     x=driver.is_title("感性的日志本")
    #     logger.info(x)
    def test_getusername(self,init_driver):
        logger.info("开始进入Im模块")
        driver = Mine(init_driver['driver'])
        driver.clickMinepage()
        w=driver.getUserName()
        logger.info(w)



