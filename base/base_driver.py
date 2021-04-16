# -*- coding:utf-8 -*-

from appium import webdriver
import time
import io
import os
import sys
import json
import urllib.request
from base.readIphoneData import readIphone,readAppData
from tomorrow3 import threads

class setdriver():
    def desired(self,iphoneData,num):
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
        appProjectData=eval(str(iphoneData[num]))
        appname=readAppData(appProjectData['project'])
        desired_caps=dict()
        #手机平台版本，大小写无所谓，对就行
        desired_caps['platformName']='Android'
        #要测试手机安卓版本（9.1.1可以写9.1 也可以写9都行）
        #desired_caps['platformVersion']=str(appProjectData['iphoneAndroidNum'])
        desired_caps['platformVersion'] = '11'
        #设备的名字，adb命令：adb devices查看，这个设备号安卓可以随便写，ios必须写对
        desired_caps['deviceName']=str(appProjectData['devices'])
        #要测试的应用的包名
        desired_caps['appPackage']=str(appname['appPackage'])
        #要启动应用的那个界面，就输入对应页面的activity
        desired_caps['appActivity']=str(appname['appActivity'])
        #加上下面两个配置项，才可以在app上输入中文
        desired_caps['unicodeKeyboard']=False
        desired_caps['resetKeyboard']=False
        #启动app时不要清楚原有的数据
        desired_caps['noReset']=True
        return desired_caps


    def startappium(self):
        #连接appiun server
        '''
        读取参数列表中数据，获取到中台返回的任务总数，
        根据总数来获取需要开启多少个appium
        :return:
        '''
        iphoneData = readIphone()
        for i in range(0,len(iphoneData)):
            iphoneData[i]=eval(iphoneData[i])
            desired = self.desired(iphoneData,i)
            appiumPort= 4723 + i
            status=os.popen("netstat -an | grep %s" % appiumPort)
            time.sleep(2)
            t1 = status.read()
            if "LISTENING" in t1:
                print("appium服务已经启动：%s" % t1)
                return (appiumPort, desired)
            else:
                #os.popen("appium -a 127.0.0.1 -p %s -U %s --no-reset" % (appiumPort, desired['deviceName']))
                return (appiumPort, desired)


    def runapp(self):
        appiumData=self.startappium()
        driver = webdriver.Remote('http://0.0.0.0:%s/wd/hub' % appiumData[0], appiumData[1])
        driver.implicitly_wait(20)
        return driver
    def iphone_desired(self):
        iphoneData = readIphone()
        for i in range(0, len(iphoneData)):
            iphoneData[i] = eval(iphoneData[i])
            desired = self.desired(iphoneData, i)
            appiumPort = 4723 + i
            return desired,appiumPort

    def endappium(self,post_num):
        '''关闭appium服务'''
        pc = sys.platform
        if pc.upper() == 'WINDOWS':
            p = os.popen('netstat  -aon|findstr {}'.format(post_num))
            p0 = p.read().strip()
            if p0 != '' and 'LISTENING' in p0:
                p1 = int(p0.split('LISTENING')[1].strip()[0:4])   # 获取进程号
                os.popen('taskkill /F /PID {}'.format(p1))   # 结束进程
                print('appium server已结束')
        elif pc == 'darwin':
            p = os.popen('lsof -i:{}'.format(post_num))
            p0 = p.read()
            print(p0)
            if p0.strip() != '':
                p1 = int(p0.split('\n')[1].split()[1])  # 获取进程号
                os.popen('kill {}'.format(p1))  # 结束进程
                print('appium server已结束')