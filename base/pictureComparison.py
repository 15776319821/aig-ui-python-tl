import os
import cv2
import numpy as np
from base.base_log import DemeLog

log=DemeLog().log()
#找图 返回最近似的点
def search_returnPoint(checkimage,baseimage):
    '''
    图片格式必须为png
    :param checkimage: 待校验图片
    :param baseimage:  原图
    :return: True 代表比对成功，False 代表在原图中无法找到待校验的图片
    '''
    try:
        filepath = os.path.dirname(os.path.abspath(__file__))
        imagefilepath = os.path.join(os.path.dirname(filepath) + "/screenShotImage")
        imagelist = os.listdir(imagefilepath)
        imageListName=[]
        for i in imagelist:
            imageName=i.split(".png")[0]
            imageListName.append(imageName)
        if checkimage not in imageListName:
            log.info("文件夹中无待校验图片！")
            return False
        elif baseimage not in imageListName:
            log.error("文件夹中无原图，无法进行比对！")
            return False
        scale = 1
        checkimage = os.path.join(imagefilepath + "/%s.png" % checkimage)
        baseimage = os.path.join(imagefilepath + "/%s.png" % baseimage)
        img = cv2.imread(checkimage)  # 要找的小图
        img = cv2.resize(img, (0, 0), fx=scale, fy=scale)
        template = cv2.imread(baseimage)  # 大图
        template = cv2.resize(template, (0, 0), fx=scale, fy=scale)
        template_size = template.shape[:2]
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        template_ = cv2.cvtColor(template,cv2.COLOR_BGR2GRAY)
        try:
            result = cv2.matchTemplate(img_gray, template_,cv2.TM_CCOEFF_NORMED)
        except Exception:
            log.error("图片比对结束，比对图片与截屏原图不符，比对图片：%s,底图%s" .format(checkimage,baseimage))
            return False
        #设置阈值
        threshold = 0.7
        # res大于70%
        loc = np.where(result >= threshold)
        # 使用灰度图像中的坐标对原始RGB图像进行标记
        #print("是否存在+",loc)
        point = ()
        for pt in zip(*loc[::-1]):
            cv2.rectangle(img, pt, (pt[0] + template_size[1], pt[1] + + template_size[0]), (7, 249, 151), 2)
            point = pt
        if point==():
            log.error("图片比对结束，比对图片与截屏原图不符，比对图片：%s,底图:%s" % (checkimage,baseimage))
            return False
        if (img is None):
            log.error("图片比对结束，未找到小图，比对图片：%s"% checkimage)
            return False
        else:
            log.info("图片比对结束，比对图片与截屏原图相符，比对图片：%s,底图:%s" % (checkimage,baseimage))
            return True
    except Exception as error:
        log.error("图片比对代码运行出现错误，错误原因： %s" % error)
if __name__ == '__main__':
    x=search_returnPoint("小图2","截屏图")
    print(x)