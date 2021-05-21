# -*- coding:utf-8 -*-
# @Time     :2019/12/8 13:34
# @Author   :zdl
# @Email    :1420500885@qq.com
# @File     :basepage.py
# @Software :PyCharm

import time
from selenium.webdriver.support.wait import WebDriverWait
from base.base_log import logger
from datetime import datetime
from base.createpath import p_path
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver

class BaseAction:
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
            findloc=WebDriverWait(self.driver,time,poll).until(lambda x:x.find_element(by,value))
            logger.info("发现{}元素".format(loc))
            return findloc
        except Exception as error:
            logger.info("无法获取{}元素，是因为{}".format(loc,error))
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
    # def save_page_screenshot(self, img_dic):
    #     """
    #     :param img_dic:  截屏的图片
    #     :return:
    #     """
    #
    #     time =datetime.now().strftime('%Y%m%d%H%M%S')
    #     screenshot_path = p_path.SCREENSHOTS_PATH+ "/{}_{}.png".format(img_dic, time)
    #     try:
    #         self.driver.get_screenshot_as_file(p_path.SCREENSHOTS_PATH+screenshot_path)
    #         self.driver.save_screenshot(screenshot_path)
    #     except Exception as err:
    #         logger.exception("当前网页截图失败")
    #     else:
    #         logger.info("截取当前网页成功并存储在:{}".format(screenshot_path))

    #断言方法a



