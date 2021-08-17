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
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    '''
    获取每个用例状态的钩子函数
    :param item:
    :param call:
    :return:
    '''
    # 获取钩子方法的调用结果
    outcome = yield
    rep = outcome.get_result()
    # 仅仅获取用例call 执行结果是失败的情况, 不包含 setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # let's also access a fixture for the fun of it
            if "tmpdir" in item.fixturenames:
                extra = " (%s)" % item.funcargs["tmpdir"]
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")
        # # 添加allure报告截图
        # if hasattr(_driver, "save_screenshot"):
        #     with allure.step('添加失败截图...'):
        #         allure.attach(_driver.save_screenshot("失败截图1.png").read(), "失败截图1", allure.attachment_type.PNG)
    else:
        return False

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
