from base.base_log import logger
from pageproject.FancyMe.im_page import Im
from elementloc.FancyMe.IM import ImLoc
import time
import pytest
import allure

class TestIntimacy():
    @allure.title("校验亲密度弹窗显示")
    @allure.story("1、点击进入一个1v1消息"
                  "2、点击亲密度按钮"
                  "3、校验弹窗显示"
                  "4、关闭弹窗并返回到消息模块页面")
    def test_intimacyCheck(self,init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.clickIntimacy()
        result = driver.is_exit(ImLoc.Im_news_1v1message_heartRate)
        assert result == True
        driver.closeIntimacyInfo()
        driver.returnBtn()
    @allure.title('校验亲密度弹窗详情显示')
    @allure.story("1、点击进入一个1v1消息"
                  "2、点击亲密度按钮"
                  "3、校验弹窗中详情显示"
                  "4、关闭弹窗并返回到消息模块页面")
    def test_intimacyInfoShow(self,init_driver):
        logger.info("开始进入Im模块")
        driver = Im(init_driver['driver'])
        time.sleep(5)
        driver.handleException()
        driver.clickImPage()
        driver.click1v1Message(clickStatus=2)
        driver.clickIntimacy()
        result = driver.is_exit(ImLoc.Im_news_1v1message_heartRateInfo)
        assert result == True
        driver.closeIntimacyInfo()
        driver.returnBtn()


