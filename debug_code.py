
'''import time
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


import os

path=os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/data/confData/")
print(path)
os.chdir(path)

import jsonpath
data={
				"code":200,
				"msg":"操作成功",
				"data":{
					"msg":"收到了1台可用手机",
					"jobs":[
							{
								"devices":"NXTDU16818005575",
								"project":"wink",
								"py":"test_msg.py",
								"tag":"v1.0"
							}
							,
							{
								"devices":"xxxx",
								"project":"cuteu",
								"py":"test111_msg.py",
								"tag":"v2.0"
							}
						]
					}
			}
y="$.." + "py"
x=jsonpath.jsonpath(data,y)
print(x)
w=" ".join(sorted(x))
print("pytest %s" % w)
'''

import appium
from appium import webdriver
desired_caps = dict()
# 手机平台版本，大小写无所谓，对就行
desired_caps['platformName'] = 'Android'
# 要测试手机安卓版本（9.1.1可以写9.1 也可以写9都行）
# desired_caps['platformVersion']=str(appProjectData['iphoneAndroidNum'])
desired_caps['platformVersion'] = '11'
# 设备的名字，adb命令：adb devices查看，这个设备号安卓可以随便写，ios必须写对
desired_caps['deviceName'] = "aR5CN90H26NK"
# 要测试的应用的包名
desired_caps['appPackage'] = "com.moonchat.date"
# 要启动应用的那个界面，就输入对应页面的activity
desired_caps['appActivity'] = "com.moonchat.date.business.main.MainActivity"
# 加上下面两个配置项，才可以在app上输入中文
desired_caps['unicodeKeyboard'] = False
desired_caps['resetKeyboard'] = False
# 启动app时不要清楚原有的数据
desired_caps['noReset'] = True
driver = webdriver.Remote('http://0.0.0.0:5037/wd/hub', desired_caps)
