# -*- coding:utf-8 -*-
import os
import time
from base.base_log import DemeLog
from datetime import datetime
from base.createpath import p_path
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logger = DemeLog().log()
class BaseAction:
    _blacklist=[(By.ID,"tips"),(By.ID,"iamge_cannel")]
    def __init__(self,driver):
        self.driver = driver
    #点击单个元素
    def click_element(self,loc,img_doc):
        try:
            self.find_element(loc).click()
            logger.info("点击元素{},{}".format(loc,img_doc))
        except Exception as error:
            logger.info("点击元素失败{}，是因为{}:{}".format(loc,error,img_doc))

    #点击多个元素中的第c个下标那个
    def click_elements(self,loc,c,img_doc):
        try:
            self.list_elements(loc,c).click()
            logger.info("点击第{}个元素,{}".format(c,loc))
        except Exception as error:
            logger.info("点击第{}个元素{}失败，是因为{}:{}".format(c,loc,error,img_doc))

    #连续点击n次,为了app能截图设计的
    def continuous_click(self,el,n):
        try:
            TouchAction(self.driver).tap(el, count=n).perform()
            logger.info("连续点击{}，{}次".format(el,n))
        except Exception as error:
            logger.info("连续点击{}失败")
    #输入文字
    def input_text(self,loc,text):
        try:
            self.find_element(loc).send_keys(text)
            logger.info("发现{}元素，且成功输入{}".format(loc,text))
        except Exception as error:
            logger.info("无法获取{}元素，并且没有输入{}文本值".format(loc,text))
    #寻找单个元素
    def find_element(self, loc,time=20,poll=1):
        by=loc[0]
        value=loc[1]
        #return self.driver.find_element(by,value)
        try:
            findloc=WebDriverWait(self.driver,time,poll).until(EC.presence_of_element_located((by,value)))
            logger.info("发现{}元素".format(loc))
            return findloc
        except Exception as error:
            logger.info("无法获取{}元素，是因为{}".format(loc,error))
            return None
    #寻找多个元素
    def find_elements(self, loc,time=20,poll=1):
        by=loc[0]
        value=loc[1]
        try:
            findlocs=WebDriverWait(self.driver, time, poll).until(lambda x:x.find_element(by,value))
            logger.info("发现{}元素".format(loc))
            return findlocs
        except Exception as error:
            logger.info("无法获取{}元素，是因为{}".format(loc,error))

    #获取多元素下标
    def list_elements(self, loc, c):
        newslist = self.find_elements(loc, c)
        list = []
        for d in newslist:
            list.append(d)
        return list[c]

    #关闭驱动
    def close(self,driver):
        self.driver.quit()

    #保存截图到outputs/screenshots需要用到
    def save_page_screenshot(self, img_dic):
        """
        :param img_dic:  截屏的图片
        :return:
        """

        time =datetime.now().strftime('%Y%m%d%H%M%S')
        screenshot_path = p_path.SCREENSHOTS_PATH+ "/{}_{}.png".format(img_dic, time)
        try:
            self.driver.get_screenshot_as_file(p_path.SCREENSHOTS_PATH+screenshot_path)
            self.driver.save_screenshot(screenshot_path)
        except Exception as err:
            logger.exception("当前网页截图失败")
        else:
            logger.info("截取当前网页成功并存储在:{}".format(screenshot_path))

    def comparisonScreenShot(self, img_dic:str):
        """
        对比图片进行底图截图模块
        :param img_dic:  截屏的图片名称
        :return:保存图片
        """

        filepath = os.path.dirname(os.path.abspath(__file__))
        imagefilepath = os.path.join(os.path.dirname(filepath) + "/screenShotImage")
        screenshot_path = imagefilepath + str(img_dic) + '.png'
        try:
            self.driver.get_screenshot_as_file(screenshot_path)
            self.driver.save_screenshot(screenshot_path)
        except:
            logger.exception("当前网页截图失败")
        else:
            logger.info("截取当前网页成功并存储在:{}".format(screenshot_path))
    def handleException(self):
        #获取异常弹窗
        # for locator in self._blacklist:
        #     elements=self.find_elements(*locator)
        #     if len(elements) >=1:
        #         elements[0].click()
        #     else:
        #         logger.info("%s not found" % str(locator))
        pageSource=self.driver.page_source
        for locator in self._blacklist:
            if locator[1] in pageSource:
                self.click_element(locator,locator)
            if "打开权限" in pageSource:
                self.click_element((By.NAME,"取消"),"关闭权限")

    def swipeToLeft(self,start_x,end_x):
        #向左滑动
        size = self.driver.get_windows_size()
        x = size['width']
        y = size['height']
        start_x = int(x * start_x)
        end_x = int(x * end_x)
        y=int(y*0.5)
        self.driver.swipe(start_x,y,end_x,y,duration=200)
    def swipeToRight(self,start_x,end_x):
        #向右滑动
        size = self.driver.get_windows_size()
        x = size['width']
        y = size['height']
        start_x = int(x * start_x)
        end_x = int(x * end_x)
        y = int(y * 0.5)
        self.driver.swipe(start_x, y, end_x, y, duration=200)
    def swipeToUp(self,start_y,end_y):
        #向上滑动
        size = self.driver.get_windows_size()
        x = size['width']
        y = size['height']
        start_y = int(y * start_y)
        end_y = int(y * end_y)
        x = int(x * 0.5)
        self.driver.swipe(x, start_y, x, end_y, duration=200)
    def swipeToDown(self,start_x,start_y,end_x,end_y):
        # 向下滑动
        size = self.driver.get_windows_size()
        x = size['width']
        y = size['height']
        start_y = int(y * start_y)
        end_y = int(y * end_y)
        x = int(x * 0.5)
        self.driver.swipe(x, start_y, x, end_y, duration=200)
    def longClick(self,locator,time=1000):
        #点击长按元素
        element=self.find_element(locator)
        TouchAction(self.driver).long_press(element,duration=time)
    def getElementEnabled(self,locator):
        #获取元素的enabled值
        element=self.find_element(locator)
        return element.is_enabled()

