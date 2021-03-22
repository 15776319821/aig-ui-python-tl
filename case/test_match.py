# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os,sys
sys.path.append(os.getcwd())
#导入启动项driver
from base.base_driver import desired
from pageproject.match_page import MatchPage
from data import msg_data
import time
import pytest


class Testmatch():
    def setup(self):
        time.sleep(5)
        self.driver=desired()
        self.match_page = MatchPage(self.driver)

    def teardown(self):
        print("第二个执行222")
        time.sleep(3)
        self.driver.quit()


    def test_msg(self):
        time.sleep(3)
        #点击消息按钮
        self.match_page.match()
        print("这是第二个的第一步：切换到消息页面")
        #self.driver.find_element_by_id('com.cuteu.videochat:id/btnTabMessage').click()
        self.match_page.msglist(1)
        print("第二个的第二步，点击进入1V1")
        time.sleep(4)

