import pytest
from base.base_log import logger
from base.base_driver import setdriver
from elementloc.FancyMe.IM import ImLoc
import os,sys
sys.path.append(os.getcwd())
import time
@pytest.fixture(scope='class')
def init_driver():
    driver = setdriver().runapp()
    yield {'driver':driver}
    time.sleep(20)
    driver.quit()
def returnBtn(self):
    logger.info("返回")
    #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

    returnBtn=ImLoc.Im_news_1v1message_returnBtn
    source=self.driver.page_source
    time.sleep(2)
    while True:
        if returnBtn[1] in source:

            self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
            logger.info("循环点击返回按钮，退出到一级页面")
        else:
            logger.info("页面返回到一级页面")
            break
def startScreenShot(dirver):
    pass
def returnBtn(self):
    logger.info("返回")
    #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

    returnBtn=ImLoc.Im_news_1v1message_returnBtn
    source=self.driver.page_source
    time.sleep(2)
    while True:
        if returnBtn[1] in source:

            self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
            logger.info("循环点击返回按钮，退出到一级页面")
        else:
            logger.info("页面返回到一级页面")
            break
def startScreenShot(dirver):
    pass
def returnBtn(self):
    logger.info("返回")
    #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

    returnBtn=ImLoc.Im_news_1v1message_returnBtn
    source=self.driver.page_source
    time.sleep(2)
    while True:
        if returnBtn[1] in source:

            self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
            logger.info("循环点击返回按钮，退出到一级页面")
        else:
            logger.info("页面返回到一级页面")
            break
def startScreenShot(dirver):
    pass
def returnBtn(self):
    logger.info("返回")
    #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

    returnBtn=ImLoc.Im_news_1v1message_returnBtn
    source=self.driver.page_source
    time.sleep(2)
    while True:
        if returnBtn[1] in source:

            self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
            logger.info("循环点击返回按钮，退出到一级页面")
        else:
            logger.info("页面返回到一级页面")
            break
def startScreenShot(dirver):
    pass
def returnBtn(self):
    logger.info("返回")
    #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

    returnBtn=ImLoc.Im_news_1v1message_returnBtn
    source=self.driver.page_source
    time.sleep(2)
    while True:
        if returnBtn[1] in source:

            self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
            logger.info("循环点击返回按钮，退出到一级页面")
        else:
            logger.info("页面返回到一级页面")
            break
def startScreenShot(dirver):
    pass
def returnBtn(self):
    logger.info("返回")
    #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

    returnBtn=ImLoc.Im_news_1v1message_returnBtn
    source=self.driver.page_source
    time.sleep(2)
    while True:
        if returnBtn[1] in source:

            self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
            logger.info("循环点击返回按钮，退出到一级页面")
        else:
            logger.info("页面返回到一级页面")
            break
def startScreenShot(dirver):
    pass
