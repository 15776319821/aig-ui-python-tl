# -*- coding:utf-8 -*-

from appium import webdriver
import time
import io
import os
import sys
import urllib.request
from base.readIphoneData import readIphone
# iphoneData=readIphone()
# for i in range(len(iphoneData)):
#     print(iphoneData[i])

#Serverurl='http://127.0.0.1:4723/wd/hub'
def desired():
    iphoneData = readIphone()
    for i in range(0,len(iphoneData)):
        iphoneData[i]=eval(iphoneData[i])
        appiumPort= 4723 + i
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
        desired_caps=dict()
        #手机平台版本，大小写无所谓，对就行
        desired_caps['platformName']='Android'
        #要测试手机安卓版本（9.1.1可以写9.1 也可以写9都行）
        desired_caps['platformVersion']=str(iphoneData[i]['iphoneAndroidNum'])
        #设备的名字，adb命令：adb devices查看，这个设备号安卓可以随便写，ios必须写对
        desired_caps['deviceName']=str(iphoneData[i]['iphoneInfo'])
        #要测试的应用的包名
        desired_caps['appPackage']='com.cuteu.videochat'
        #要启动应用的那个界面，就输入对应页面的activity
        desired_caps['appActivity']='com.cuteu.video.chat.business.splash.SplashActivity'
        #加上下面两个配置项，才可以在app上输入中文
        desired_caps['unicodeKeyboard']=True
        desired_caps['resetKeyboard']=True
        #启动app时不要清楚原有的数据
        desired_caps['noReset']=True

        #连接appiun server，其中http的地址直接就是这个格式，没什么好说的
        driver = webdriver.Remote('http://127.0.0.1:%s/wd/hub' %appiumPort,desired_caps)
        driver.implicitly_wait(2)
        return driver
if __name__ == '__main__':
    desired()