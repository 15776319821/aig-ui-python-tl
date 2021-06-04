from base.base_log import logger
from pageproject.FancyMe.im_page import Im
from pageproject.FancyMe.mine_page import Mine
from base.base_action import BaseAction
import time
import allure
class Test_userInfo():
    @allure.title("1、进入我的模块"
                  "2、获取用户昵称"
                  "3、进入用户信息设置页面，校验页面跳转正常"
                  "4、校验用户信息设置页面昵称与主页面显示昵称一直")
    def test_getusername(self, init_driver):
        logger.info("开始进入我的模块")
        driver = Mine(init_driver['driver'])
        driver.clickMinepage()
        userName = driver.getUserName()
        driver.clickUserInfo()
        userInfoTitle=driver.userInfoTitle()
        assert userInfoTitle == "编辑资料"


