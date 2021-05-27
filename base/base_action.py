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
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

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
            return True
        except Exception as error:
            logger.info("点击元素失败{}，是因为{}:{}".format(loc,error,img_doc))
            return None

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
            logger.info("连续点击{}元素{}次失败,是因为{}".format(el,n,error))
    #输入文字
    def input_text(self,loc,text,img_doc):
        try:
            self.find_element(loc).send_keys(text)
            logger.info("发现{}元素，且成功输入{},{}".format(loc,text,img_doc))
        except Exception as error:
            logger.info("无法获取{}元素，并且没有输入{}文本值,是因为{}".format(loc,text,error))
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
            findlocs=WebDriverWait(self.driver, time, poll).until(lambda x: x.find_elements(by, value))
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

    # 关闭驱动
    # def close(self,driver):
    #     self.driver.quit()

    #判断元素是否存在---单个元素
    def is_elementloc(self,loc):
        try:
            self.driver.find_element(*loc)
            return True
        except Exception as erro:
            logger.info('没有这个元素{},报错{}'.format(loc,erro))
            return False

    #判断元素是否存在---多个元素
    def is_elmentsloc(self,loc):
        try:
            self.driver.find_elements(*loc)
            return True
        except Exception as erro:
            logger.info('查找不到这些元素，报错{}'.format(erro))
            return False

        # else:
        #     try:
        #         if element is None:
        #             logger.info('else层的日志输出，没有这个元素')
        #             return True
        #         else:
        #             logger.info('==================test test================')
        #             return False
        #     except Exception as e:
        #         logger.info('是不是走到TURE了！！')
        #         return True

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
                self.click_element((By.ID,"android:id/button2"),"关闭权限")
                break

    def swipeToLeft(self,start_x,end_x,swipeNum=1):
        #向左滑动
        num=0
        size=WebDriver.get_window_size(self.driver)
        x = size['width']
        y = size['height']
        start_x = int(x * start_x)
        end_x = int(x * float(end_x))
        y=int(y*0.5)
        while num <= swipeNum:
            self.driver.swipe(start_x,y,end_x,y,duration=2000)
            num += 1
    def swipeToRight(self,start_x,end_x,swipeNum=1):
        #向右滑动
        num = 0
        size=WebDriver.get_window_size(self.driver)
        x = size['width']
        y = size['height']
        start_x = int(x * start_x)
        end_x = int(x * end_x)
        y = int(y * 0.5)
        while num <= swipeNum:
            self.driver.swipe(start_x, y, end_x, y, duration=2000)
            num += 1
    def swipeToUp(self,start_y,end_y,swipeNum=1):
        #向上滑动
        num=0
        size=WebDriver.get_window_size(self.driver)
        x = size['width']
        y = size['height']
        start_y = int(y * start_y)
        end_y = int(y * end_y)
        x = int(x * 0.5)
        while num <= swipeNum:
            self.driver.swipe(x, start_y, x, end_y, duration=2000)
            num += 1
    def swipeToDown(self,start_y,end_y,swipeNum=1):
        # 向下滑动
        num=0
        size=WebDriver.get_window_size(self.driver)
        x = size['width']
        y = size['height']
        start_y = int(y * start_y)
        end_y = int(y * end_y)
        x = int(x * 0.5)
        while num <= swipeNum:
            self.driver.swipe(x, start_y, x, end_y, duration=2000)
            num += 1
    def longClick(self,locator,time=1000):
        #点击长按元素
        if locator[0] == 'id':
            element = self.driver.find_element_by_id(locator[1])
        elif locator[0] == 'xpath':
            element = self.driver.find_element_by_xpath(locator[1])

        TouchAction(self.driver).long_press(element,duration=time)
    def getElementEnabled(self,locator):
        #获取元素的enabled值
        try:
            element=self.find_element(locator)
            return element.is_enabled()
        except TimeoutException:
            raise ElementNotVisibleException("元素未找到 %s" % locator)
    def is_exite_sys(self,locator):
        #判断元素是否在页面
        pageSource = self.driver.page_source
        if locator[1] in pageSource:
            return True
    def childSelector(self,locator,locator2):
        #根据父节点定位子节点
        driver = WebDriver(self.driver)
        element = driver.find_element_by_xpath(locator[1]).child(locator2[1])
        return element
    def parentSelector(self,locator,locator2):
        #返回当前节点的父节点
        element = self.driver.find_element_by_xpath(locator[1]).parent(locator2[1])
        return element
    def preceding_sibling(self,locator,locator2):
        #兄弟节点定位
        driver = WebDriver(self.driver)
    def getElementText(self,loc):
        method=loc[0]
        element=loc[1]
        try:
            if method == 'id':
                ele = self.driver.find_element_by_id(element).text
                return ele
            if method == 'xpath':
                ele = self.driver.find_element_by_xpath(element).text()
                return ele
        except:
            raise ElementNotVisibleException("无法获取元素文本，查询是否元素出错 ", element)

    def find_ele(self,loc):

        try:
            if loc[0] == 'id':
                ele = self.driver.find_element_by_id(loc[1])
                return ele
        except:
            raise ElementNotVisibleException("无法寻找到该元素")
    def click_ele(self,loc):
        try:
            ele=self.find_ele(loc)
            ele.click()
        except:
            raise ElementNotVisibleException('无法点击元素！')
    def find_element_xpath(self,loc):
        method=loc[0]
        element=loc[1]
        if method == 'id':
            try:
                ele = self.driver.find_element_by_xpath("//input[@id= %s]" % element)
                return ele
            except:
                raise ElementNotVisibleException("无法寻找到该元素")
    def is_title(self,title=''):
        try:
            result = WebDriverWait(self.driver, timeout=10).until(EC.title_is(title))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value=''):
        """返回bool值，value为空字符串，返回False"""
        try:
            result = WebDriverWait(self.driver, timeout=20).until(
                EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False
    def is_exit(self,loc):
        try:
            self.find_element(loc)
            return True
        except:
            return False
    def is_alert(self, timeout=3,t=0.5):
        try:
            result = WebDriverWait(self.driver, timeout,t).until(EC.alert_is_present())
            return result
        except:
            return False







