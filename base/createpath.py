# -*- coding:utf-8 -*-

import os


class ProjectPath:
    # 项目路径
    ROOT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # outputs路径
    OUTPUTS_PATH = os.path.join(ROOT_PATH, 'outputs')
    # reports路径
    REPORTS_PATH = os.path.join(OUTPUTS_PATH, 'reports')
    # 日志路径
    LOGS_PATH = os.path.join(OUTPUTS_PATH, 'log')
    # 截图路径
    SCREENSHOTS_PATH = os.path.join(OUTPUTS_PATH, 'screenshots')


    # 如果没有改文件夹，自动创建
    if not os.path.exists(REPORTS_PATH):
        os.mkdir(REPORTS_PATH)
    if not os.path.exists(LOGS_PATH):
        os.mkdir(LOGS_PATH)
    if not os.path.exists(SCREENSHOTS_PATH):
        os.mkdir(SCREENSHOTS_PATH)


p_path = ProjectPath()