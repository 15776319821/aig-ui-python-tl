from pageproject.match_page import MatchPage
from base.base_log import logger
from base.base_action import BaseAction
from elementloc.FancyMe.IM import ImLoc
import time
class Im(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def clickImPage(self):
        '''
        进入消息模块
        :return:
        '''
        logger.info("开始执行进入IM模块")
        self.find_element(ImLoc.Im_loc,'消息模块元素')
        self.click_element(ImLoc.Im_loc,'点击消息模块')
        logger.info("进入消息模块")
    def clickImManageList(self):
        '''
        点击消息处理按钮,校验打开正确
        :return:  true
        '''
        logger.info("点击消息模块消息处理弹窗按钮")
        self.find_element(ImLoc.Im_news_manage_handleList,'消息处理弹窗按钮')
        self.click_element(ImLoc.Im_news_manage_handleList,'消息处理弹窗按钮')

        if self.is_exite(ImLoc.Im_news_manage_deleteMessageBtn):
            logger.info("消息处理弹窗显示")
        else:
            logger.info('消息处理弹窗未出现')
    def closeClickImManageList(self):
        '''
        关闭消息统一处理弹窗
        :return:
        '''
        #关闭消息页面统一处理弹窗
        closeBtn=ImLoc.Im_news_manage_closeAlert
        self.find_element(closeBtn,'关闭消息处理按钮')
        if self.is_exite(closeBtn):
            logger.info("弹窗关闭")

    def clickTeamMessage(self,click=1):
        '''
        校验团队信是否存在
        :param click: 不等于1时，点击进入团队信
        :return:
        '''
        logger.info("查询团队信是否存在")
        self.find_element(ImLoc.Im_team,'团队信消息存在')
        if click != 1:
            logger.info("点击进入消息团队信页面")
            self.click_element(ImLoc.Im_team,'消息团队信')

    def clickNoticeMessage(self,click=1):
        '''
        校验互动消息是否存在
        :param click: 不等于1时，点击进入互动消息
        :return:
        '''
        logger.info("互动消息按钮显示")
        self.find_element(ImLoc.Im_notice,"互动消息显示正常")
        if click != 1:
            logger.info("点击进入互动消息页面")
            self.click_element(ImLoc.Im_notice,"互动消息")

    def click1v1Message(self,clickStatus=1):
        '''
        校验1v1消息最后时间是否存在
        :param click: 不等于1时，点击最后时间
        :return:
        '''
        logger.info("消息列表信息")
        try:
            self.find_elements(ImLoc.Im_news_lastTime,"1v1消息最后时间",1)
        except:
            raise AssertionError
        if clickStatus != 1:
            logger.info("点击最后消息时间")
            self.click_elements(ImLoc.Im_news_lastTime,1,"1v1消息最后时间")
            if self.find_element(ImLoc.Im_news_1v1message_btnReply,"1v1消息预设置按钮"):
                logger.info("进入1v1消息页面")

    def getRecevMessage(self,num):
        #点击聊天列表中的一个
        try:
            self.click_elements(ImLoc.Im_news_1v1message_revceMessage,num,'点击聊天列表')
        except:
            raise AssertionError

    def clickFriend(self):
        '''
        点击好友按钮
        :return:
        '''
        self.click_element(ImLoc.Im_friedButton,'点击好友列表')
        if self.is_exite(ImLoc.Im_news_friedPage_friedList):
            logger.info("跳转好友列表成功")



    def returnBtn(self):
        '''
        无限返回，当返回按钮在页面中时，则持续点击
        :return:
        '''
        logger.info("返回")
        while True:
            if self.is_exite(ImLoc.Im_news_1v1message_returnBtn):

                self.click_element(ImLoc.Im_news_1v1message_returnBtn, '返回按钮')
                logger.info("循环点击返回按钮，退出到一级页面")
            else:
                logger.info("页面返回到一级页面")
                break
    def leftPage(self):
        self.swipeToLeft(start_x=0.7,end_x=0.3)

    def messageClickVioce(self):
        '''点击语音通话按钮'''
        element=self.click_element(ImLoc.Im_news_1v1messsage_sendVoiceCall,'语音通话按钮')

    def messageClickVideo(self):
        '''点击视频通话按钮'''
        self.find_element(ImLoc.Im_news_1v1messsage_sendVideoCall,'视频通话按钮')
    def messageClickSendPicture(self):
        '''点击发送图片按钮'''
        self.find_element(ImLoc.Im_news_1v1messsage_sendPicBtn,'图片按钮')
    def messageClicksendSecretPicture(self):
        '''点击私密照片按钮'''
        self.find_element(ImLoc.Im_news_1v1messsage_sendSecretBtn,'私密照片按钮')
    def checkHandle(self):
        '''校验无亲密度拦截弹窗'''
        if self.find_ele(ImLoc.Im_news_1v1message_heartRateLessAlert[0],ImLoc.Im_news_1v1message_heartRateLessAlert[1]):
            logger.info("亲密度不足弹窗显示")
            self.click_element(ImLoc.Im_news_1v1message_heartRateLessAlertCloseBtn,'关闭亲密度不足弹窗')
            return True
        else:
            raise AssertionError
    def checkMessageTitle(self):
        pass
    def clickIntimacy(self):
        #点击亲密度按钮
        self.find_element(ImLoc.Im_news_1v1message_intimacyBtn,'亲密度查询按钮')
        self.click_element(ImLoc.Im_news_1v1message_intimacyBtn,'亲密度查询按钮')
    def closeIntimacyInfo(self):
        self.click_element(ImLoc.Im_news_1v1message_heartRateAlertCloseBtn,'亲密度详情弹窗关闭按钮')


    def clickIm(self):
        '''
        进入消息模块
        :return:
        '''
        logger.info("开始执行进入IM模块")
        self.find_ele(ImLoc.Im_loc)
        self.click_element(ImLoc.Im_loc,'点击消息模块')
        logger.info("进入消息模块")













