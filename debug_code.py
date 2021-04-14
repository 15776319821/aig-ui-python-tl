import time
from base.base_action import BaseAction
from base.base_driver import setdriver
from appium import webdriver
x=setdriver().runapp()
#x=(4723,{'platformName': 'Android', 'platformVersion': '11', 'deviceName': 'R5CN90H26NK', 'appPackage': 'com.cuteu.videochat', 'appActivity': 'com.cuteu.video.chat.business.splash.SplashActivity', 'unicodeKeyboard': False, 'resetKeyboard': False, 'noReset': True})
#driver = webdriver.Remote('http://0.0.0.0:%s/wd/hub' % x[0], x[1])
print(x)
time.sleep(10)
x.find_element_by_id("com.cuteu.videochat:id/btnTabMessage").click()


#<appium.webdriver.webdriver.WebDriver (session="1a0e23b4-1ad3-410d-98f5-4e24c036a466")>

