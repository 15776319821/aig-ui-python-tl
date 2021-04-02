# -*- coding:utf-8 -*-
# @Time     :2021/2/18 19:51
# @Author   :wjl
# @Email    :753538091@qq.com
# @File     :basepage.py
# @Software :PyCharm

import logging
import time
import os

class DemeLog():


    def log(self):
        #创建一个日志器
        Logger=logging.getLogger("logger")

        #设置日志输出的最低等级
        Logger.setLevel(logging.DEBUG)
        if not Logger.handlers:

            #创建一个处理器——在控制台输出
            sh=logging.StreamHandler()
            #创建一个处理器——保存成文件
            filepath=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            filename=os.path.join(filepath + "/outputs/log/{}_log".format(time.strftime('%Y_%m_%d_%H_%M')))
            fh=logging.FileHandler(filename=filename,encoding='utf-8')
            #保存成文件和在控制台输出不一样的就是需要写清楚文件保存的路径和文件名字的格式，而控制台不需要这些


            #创建一个格式器,负责日志显示的格式
            formatter=logging.Formatter(fmt='%(asctime)s %(filename)s %(levelname)s %(message)s',
                                        datefmt='%Y/%m/%d/%X')
            #因为fmt中有asctime（时间），所以要有datefmt目的是来指定时间格式的显示样式
            #绑定格式器到处理器上去
            sh.setFormatter(formatter)
            fh.setFormatter(formatter)
            #绑定处理器到日志器上面（因为一个日志器可以有多个处理器）
            Logger.addHandler(sh)
            Logger.addHandler(fh)
        return Logger

"""
        #下面就是设置你想输出的日志的等级
        Logger.debug('debug msg')
        Logger.info('info msg')
        Logger.warning('warning msg')
        Logger.error('error信息')
        Logger.critical('critical msg')
"""




logger =DemeLog().log()
