#!/bin/bash
import time
import requests
import os
import json
import sys
from UIDeskTop.getGitFile import gitPull
class sendAdb():
    '''获取当前adb连接的手机'''
    def __init__(self):

        try:
            #adbKill=os.popen("adb kill-server")
            #time.sleep(2)
            #adbRestart=os.popen("adb start-server")
            #time.sleep(4)
            #获取当前连接的手机
            adbResult=os.popen("adb devices").read()
            #print(adbResult)
            adbResult=str(adbResult)
            adbInfo=adbResult.split("\n")
            self.iphoneInfo=adbInfo[1].split("\t")[0].strip()
            #获取当前手机型号
            self.iphoneName = os.popen("adb -d shell getprop ro.product.model").read().strip()
            #获取当前手机品牌
            self.iphoneModel = os.popen("adb -d shell getprop ro.product.brand").read().strip()
            # 获取分辨率
            iphoneSize = os.popen("adb shell wm size").read()
            self.iphoneSize=iphoneSize.split(":")[1].strip()
            # 获取cpu型号
            self.iphoneCpu = os.popen("adb shell getprop ro.product.cpu.abi").read().strip()
            # 获取手机安卓版本
            self.iphoneAndroidNum = os.popen("adb shell getprop ro.build.version.release").read().strip()
            #获取当前手机状态
            self.iphoneStatus=adbInfo[1].split("\t")[1].strip()
            if self.iphoneStatus == 'device':
                self.iphoneStatus = 0
            else:
                self.iphoneStatus = 1
        except Exception as error:
            print("adb连接出错，请查看adb命令与环境！错误信息：%s" % error)

    def sendreq(self,iphoneStatus=0,*args,**kwargs):
        '''向中台传输手机信息'''
        datas={"devices":json.dumps([{
            "android":self.iphoneAndroidNum,
            "screen":self.iphoneSize,
            "device":self.iphoneInfo,
            "cpu":self.iphoneCpu,
            "manufacturer":self.iphoneModel,
            "brand":self.iphoneName,
            "type":iphoneStatus

            }])
        }
        #print(datas)

        header={"Content-Type":"application/x-www-form-urlencoded"}
        try:
            url='http://192.168.51.206:29000/collect/receiver/'
            reportIphoneData = requests.post(url=url,data=datas,headers=header)
            reprotRspon = reportIphoneData.json()
            print(reprotRspon)
            return reprotRspon
        except Exception as e:
            print("接口传输错误！")
    def testPlan(self,uiTestPlanNum):

        '''获取当前电脑环境,如果是mac本则在桌面生成一个txt文件储存测试任务，
        windows环境则在D盘生成一个文件夹里面生成一个txt文件。
        '''
        computerSysterm = sys.platform
        if computerSysterm == 'darwin':
            os.chdir(r'/Users/aig/Desktop')
            f = open('testPlan.txt', 'w+', encoding='utf-8')
            for uiPlan in uiTestPlanNum:
                print(type(uiPlan))
                uiPlan = str(uiPlan)
                f.writelines(uiPlan + '\n')
            f.flush()
            f.close()
            f = open('testPlan.txt', 'r', encoding='utf-8')
            w = f.read()
            return w
        elif computerSysterm == 'win32':
            testPlanPath = (r'D:/DHN')
            if not os.path.exists(testPlanPath):
                os.mkdir("D:/DHN")
            os.chdir(r'D:/DHN')
            f = open('testPlan.txt', 'w+', encoding='utf-8')
            for uiPlan in uiTestPlanNum:
                print(type(uiPlan))
                uiPlan = str(uiPlan)
                f.writelines(uiPlan + '\n')
            f.flush()
            f.close()
            f = open('testPlan.txt', 'r', encoding='utf-8')
            w = f.read()
            return w

    def adbDataYaml(self):
        '''将本地手机的信息储存到yaml文件中'''
        DataYaml={}
        DataYaml['iphoneAndroidNum']=self.iphoneAndroidNum
        DataYaml['iphoneInfo'] = self.iphoneInfo

        if sys.platform == "windows":
            confDataPath = (r'D:/DHN/UIgit/aig-ui-python/data/confData')
            if not os.path.exists(confDataPath):
                os.mkdir(r'D:/DHN/UIgit/aig-ui-python/data/confData')
            os.chdir(r'D:/DHN/UIgit/aig-ui-python/data/confData/')
            f = open('confData.yaml', 'w+', encoding='utf-8')
            f.writelines(str(DataYaml) + '\n')
            f.flush()
            f.close()

        if sys.platform == 'darwin':
            confDataPath = (r'/Users/aig/Documents/UIgit/aig-ui-python/data/confData')
            if not os.path.exists(confDataPath):
                os.mkdir(r'/Users/aig/Documents/UIgit/aig-ui-python/data/confData/')
            os.chdir(r'/Users/aig/Documents/UIgit/aig-ui-python/data/confData/')
            f = open('confData.yaml', 'w+', encoding='utf-8')
            f.writelines(str(DataYaml) + '\n')
            f.flush()
            f.close()
    def runData(self):
        '''获取中台返回数据'''
        try:
            reprotRspon = self.sendreq()
            if reprotRspon['code'] != 200:
                print("中台接口服务出现问题，查看中台服务！")
            #elif reprotRspon['status'] == 500:
                #print("查看传参参数有错误！")
            elif len(reprotRspon['data']['jobs']) == 0:
                print("当前无自动化任务！")

            else:
                '''当有任务时，去git拉取最新版本代码'''
                reprotNum=reprotRspon['data']['jobs']
                gitresult=gitPull(reprotNum)
                if gitresult == True:
                    self.adbDataYaml()
                    time.sleep(2)
                    uiTestPlanIphone = reprotRspon['data']['jobs'][0]['devices']
                    '''此处暂定获取到任务后再次传送当前连接手机信息，未优化完成（未增加锁死功能）'''
                    if uiTestPlanIphone == self.iphoneInfo:
                        iphoneStatus=1
                        sendAdb().sendreq(iphoneStatus)
                    else:
                        sendAdb()

                else:
                    print("git拉取失败")
                    quit()
        except Exception as e:
            print("程序运行出现错误，错误原因： %s" .format(e))




if __name__ == '__main__':
    x=sendAdb()
    #x.adbDataYaml()
    x.runData()
