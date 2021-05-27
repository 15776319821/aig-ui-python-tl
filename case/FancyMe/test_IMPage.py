from base.base_log import logger
from pageproject.FancyMe.im_page import Im
import time
import pytest
import allure
class TestIm():

    @allure.title("进入IM")
    def test_clickImPage(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
    @allure.title("在消息页面，进入好友列表页面，右向左滑动后返回消息模块")
    @allure.step("1、进入IM"
                  "2、打开IM模块中关系列表"
                  "3、进入关系列表，右向左滑动一次"
                  "4、返回IM模块主页")
    def test_clickImPageFried(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(3)
        driver.handleException()
        driver.clickImPage()
        driver.clickFriend()
        driver.leftPage()
        driver.returnBtn()
    @allure.title("校验消息统一处理弹窗出现")
    @allure.step("1、进入IM"
                  "2、打开IM模块中关系列表"
                  "3、打开消息统一处理弹窗，并校验"
                  "4、关闭弹窗"
                  )
    def test_clickImPageManageList(self,init_driver):
        logger.info("开始执行进入IM模块")
        driver=Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.clickImManageList()
        driver.closeClickImManageList()
        driver.returnBtn()
    @allure.title("校验消息统一处理弹窗出现")
    @allure.step("1、进入IM模块"
                  "2、点击进入一个聊天列表。"
                  "3、点击视频通话"
                  "4、验证无亲密度情况下，弹窗正确")
    def test_clickVideo(self,init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.messageClickVideo()
        status=driver.checkHandle()
        assert status == True
        driver.returnBtn()

    @allure.title("无亲密度情况下发送视频电话，验证拦截弹窗出现")
    @allure.step("1、进入IM模块"
                  "2、点击进入一个聊天列表。"
                  "3、点击视频通话"
                  "4、验证无亲密度情况下，弹窗正确")
    def test_clickVideo(self, init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.messageClickVideo()
        status = driver.checkHandle()
        assert status == True
        driver.returnBtn()
    @allure.title("无亲密度情况下发送语音电话，验证拦截弹窗出现")
    @allure.step("1、进入IM模块"
                  "2、点击进入一个聊天列表。"
                  "3、点击语音通话"
                  "4、验证无亲密度情况下，弹窗正确")
    def test_clickVioce(self, init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.messageClickVioce()
        status = driver.checkHandle()
        assert status == True
        driver.returnBtn()
    @allure.title("无亲密度情况下发送照片，验证拦截弹窗出现")
    @allure.step("1、进入IM模块"
                  "2、点击进入一个聊天列表。"
                  "3、点击发送图片"
                  "4、验证无亲密度情况下，弹窗正确")
    def test_sendPicture(self, init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.messageClickSendPicture()
        status = driver.checkHandle()
        assert status == True
        driver.returnBtn()
    @allure.title("无亲密度情况下发送私密照片，验证拦截弹窗出现")
    @allure.step("1、进入IM模块"
                  "2、点击进入一个聊天列表。"
                  "3、点击发送私密照片"
                  "4、验证无亲密度情况下，弹窗正确")
    def test_sendSecretPicture(self, init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.messageClicksendSecretPicture()
        status = driver.checkHandle()
        assert status == True
        driver.returnBtn()
    def test_1v1messageTitle(self,init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()






