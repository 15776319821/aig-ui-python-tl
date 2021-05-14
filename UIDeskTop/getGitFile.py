import os
import sys
from git.repo import Repo

def gitPull(job):
    '''获取当前电脑环境，去拉取git最新代码'''
    tag = job[0]['tag']
    computerSysterm = sys.platform
    if computerSysterm == 'darwin':
        path = (r'~/Documents/UIgit/aig-ui-python')
        if not os.path.exists(path):
            os.mkdir(path)
        down_path = os.chdir(r'~/Documents/UIgit/aig-ui-python')
        repo = Repo(down_path)
        os.popen("git checkout -b test %s" .format(tag))
        x=repo.git.pull()
        if x == 'Already up to date.':
            return True
        else:
            return None
    elif computerSysterm == 'win32':
        path = (r'D:/DHN/UIgit')
        if not os.path.exists(path):
            os.mkdir(path)
        repo = Repo(path)
        x = repo.git.pull()
        print(x)
        if x == 'Already up to date.':
            return True
        else:
            return None

def code_path(computersys='mac'):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)) + "/UIDeskTop")
    print(filepath)
    f = open("path.yaml", "r", encoding="utf-8")
    Data = f.read()
    iphoneDataSet = yaml.load(Data, Loader=yaml.FullLoader)
    if sys == 'mac':
        return iphoneDataSet['path']['mac_code_path']
    else:
        return iphoneDataSet['path']['windows_code_path']



