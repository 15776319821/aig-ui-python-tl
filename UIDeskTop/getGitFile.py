import os
import sys
from git.repo import Repo

def gitPull(job):
    '''获取当前电脑环境，去拉取git最新代码'''
    jobNum=len(job)
    #for Num in range(0,jobNum):
    tag = job[0]['tag']
    computerSysterm = sys.platform
    if computerSysterm == 'darwin':
        down_path = os.chdir(r'/Users/aig/Documents/UIgit/aig-ui-python')
        repo = Repo(down_path)
        os.popen("git checkout -b test %s" .format(tag))
        x=repo.git.pull()
        print(x)
        if x == 'Already up to date.':
            return True
        else:
            return None
    elif computerSysterm == 'win32':
        Path = (r'D:/DHN/UIgit')
        repo = Repo(Path)
        x = repo.git.pull()
        print(x)
        if x == 'Already up to date.':
            return True
        else:
            return None

if __name__ == '__main__':
    x=gitPull()
    print(x)
