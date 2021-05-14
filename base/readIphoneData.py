import yaml
import os
from base.base_log import DemeLog
from selenium import webdriver
log=DemeLog().log()
def readIphone():
    '''获取手机配置信息，返回手机adb号与安卓版本'''
    rootPath=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    filePath=os.path.join(rootPath + "/data/confData/")
    os.chdir(filePath)
    f = open("confData.yaml","r",encoding="utf-8")
    iphoneDataSet=f.readlines()
    return iphoneDataSet


def readAppData(appname):
    '''获取app信息'''
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    filePath = os.path.join(rootPath + "/data/")
    os.chdir(filePath)
    f = open("appData.yaml","r",encoding="utf-8")
    Data = f.read()
    iphoneDataSet = yaml.load(Data,Loader=yaml.FullLoader)
    return iphoneDataSet[appname]
class apkConfig:
    '''apk下载与删除方法'''
    def __init__(self):
        rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) #根目录
        self.apkPath=os.path.join(rootPath + '/data/appPackage')
        if not os.path.exists(self.apkPath):
            os.mkdir(self.apkPath)

    def getApkName(self,appname='FancyU',appbuild='217000'):
        appNameList=[]
        '''获取apkPath文件下apk文件,查询符合查询逻辑的app名称'''
        for i in os.listdir(self.apkPath):
            appNameList.append(i)
        for apkname in appNameList:
            if apkname.find(appname) >=0 and apkname.find(appbuild) >=0:
                    return apkname
    def getApkPath(self,appname='FancyU',appbuild='217000'):
        '''获取到符合逻辑的apk名称后，添加完整路径'''
        apkName=self.getApkName(appname,appbuild)
        return os.path.join(self.apkPath +'/' +apkName)
    def delApk(self,appname='FancyU',appbuild='217000'):
        '''删除指定项目下指定build的apk包'''
        try:
            os.remove(self.getApkPath(appname,appbuild))
        except Exception as e:
            return ('apk未删除，错误原因 %s' % e )
    def downloadApk(self):
        '''下载apk'''
        pass
def permissionPopupClose(driver):
    #根据名称进行点击权限弹窗
    while True:
        if "允许" in driver.page_source():
            driver.switch_to.alert.accept()
        else:
            print('权限处理结束')
            break
def permissionPopupClose2(driver):
    #获取弹窗中允许的xpath,获取当前页面元素判断是否包含允许字符，有则点击xpath
    while True:
        loc = ("xpath", "//android.widget.Button[contains(@text,'允许')]")
        if '允许' in driver.page_source():
            driver.click_element(loc)
        else:
            print("权限处理结束")
            break