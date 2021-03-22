# -*- coding:utf-8 -*-
#引用自己的模块就要用到下面的这个不然报错找不到模块
import os,sys

import time

sys.path.append(os.getcwd())
from pageproject.aboutus_page import AboutUs
from base.base_driver import desired
from base.base_action import BaseAction

#为了截图

class Testabout():

    def setup(self):
        self.driver=desired()
        self.aboutus_page=AboutUs(self.driver)


    def teardown(self):
        time.sleep(5)
        self.driver.quit()

    def test_about(self):
        self.aboutus_page.Us(20)

    #BaseAction.close()
