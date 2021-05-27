from base.base_log import logger
from base.base_action import BaseAction
from elementloc.FancyMe.IM import ImLoc
from elementloc.FancyMe.MineInfo import MineLoc
import time

class Base_(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)
    def backBtn(self,num=1):
        try:
            start = 1
            while start <= num:
                self.click_element(MineLoc.Mine_backBtn,'返回按钮')
                start += 1
        except Exception as e:
            logger.info("返回出现错误")

    def startFindUser(self):
        try:
            self.find_element(MineLoc.Mine,'我的模块')
            self.click_element(MineLoc.Mine,'点击我的模块')
            self.click_element(MineLoc.Mine_settingBtn,'设置按钮')
            self.click_element(MineLoc.Mine_setting_setOurBtn,'关于我们')
            self.click_elements(MineLoc.Mine_setting_setOurPage_easterEgg,7,'7下开启彩蛋')
            self.backBtn()
        except Exception as e:
            logger.info("开启彩蛋出错，错误原因 ： ",e)


