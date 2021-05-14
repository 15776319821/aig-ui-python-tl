#!/bin/bash
import time
import requests
import os
import json
import sys
import jsonpath
from UIDeskTop.getGitFile import gitPull,code_path
from base.base_driver import setdriver
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

        header={"Content-Type":"application/x-www-form-urlencoded"}
        try:
            url='http://192.168.51.206:29000/collect/receiver/'
            reportIphoneData = requests.post(url=url,data=datas,headers=header)
            reprotRspon = reportIphoneData.json()
            print(reprotRspon)
            return reprotRspon
        except Exception as e:
            print("接口传输错误！")
            '''
    def testPlan(self,uiTestPlanNum):

        '''#获取当前电脑环境,如果是mac本则在桌面生成一个txt文件储存测试任务，
        #windows环境则在D盘生成一个文件夹里面生成一个txt文件。
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
'''
    def adbDataYaml(self,uiTestPlanNum):
        '''
        获取当前电脑环境,如果是mac本则生成一个yaml文件储存测试任务，
        windows环境则生成一个文件夹里面生成一个yaml文件。
        '''
        code_Path=code_path()
        if sys.platform == "windows":
            confDataPath=os.path.join(code_Path(computersys='windows') + "/data/confData/")
            if not os.path.exists(confDataPath):
                os.mkdir(confDataPath)
            os.chdir(confDataPath)
            f = open('confData.yaml', 'w+', encoding='utf-8')
            for uiPlan in uiTestPlanNum:
                print(type(uiPlan))
                uiPlan = str(uiPlan)
                f.writelines(uiPlan + '\n')
            f.flush()
            f.close()

        if sys.platform == 'darwin':
            confDataPath=os.path.join(code_Path() + "/data/confData/")
            #confDataPath = (r'/Users/aig/Documents/UIgit/aig-ui-python/data/confData')
            if not os.path.exists(confDataPath):
                os.mkdir(confDataPath)
            os.chdir(confDataPath)
            f = open('confData.yaml', 'w+', encoding='utf-8')
            for uiPlan in uiTestPlanNum:
                print(type(uiPlan))
                uiPlan = str(uiPlan)
                f.writelines(uiPlan + '\n')
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
                return None

            else:
                '''当有任务时，去git拉取最新版本代码'''
                reprotNum=reprotRspon['data']['jobs']
                gitresult=gitPull(reprotNum)
                if gitresult == True:
                    self.adbDataYaml(reprotRspon)
                    time.sleep(2)
                    uiTestPlanIphone = reprotRspon['data']['jobs'][0]['devices']
                    '''此处获取当前有任务的手机，并将手机状态修改为1，传回中台，中台默认status=1，为占用状态'''
                    if uiTestPlanIphone == self.iphoneInfo:
                        iphoneStatus=1
                        sendAdb().sendreq(iphoneStatus)
                    else:
                        sendAdb()
                    return reprotRspon

                else:
                    print("git拉取失败")
                    quit()
        except Exception as e:
            print("程序运行出现错误，错误原因： %s" .format(e))


    def readRunProject(self):
        #respone=self.runData()

        #中台好了在注销，未好时先注掉上面的调用
        respone={
				"code":200,
				"msg":"操作成功",
				"data":{
					"msg":"收到了1台可用手机",
					"jobs":[
							{
								"devices":"NXTDU16818005575",
								"project":"fancyme",
								"py":"test_startApp.py",
								"tag":"v1.0"
							}
						]
					}
			}

        uiTestPlanProject = jsonpath.jsonpath(respone,"$..project")
        uiTestPlanWork = jsonpath.jsonpath(respone,"$..py")
        uiTestPlan=" ".join(sorted(uiTestPlanWork))
        #此处需要修改文件路径，获取path.yaml中的路径，调试情况，没加
        os.chdir(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "/case/" + uiTestPlanProject[0]))
        os.popen("chmod +x %s" % uiTestPlan)
        print("python3 -m pytest %s" % uiTestPlan)
        os.system("python3 -m pytest %s" % uiTestPlan)

if __name__ == '__main__':
    x=sendAdb()
    #x.adbDataYaml()
    x.readRunProject()
