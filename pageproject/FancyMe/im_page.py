from pageproject.match_page import MatchPage
from base.base_log import logger
from base.base_action import BaseAction
from elementloc.FancyMe.IM import ImLoc
import time
class Im(BaseAction):

    def __init__(self, driver):
        BaseAction.__init__(self, driver)

    def clickImPage(self):
        logger.info("开始执行进入IM模块")
        self.find_element(ImLoc.Im_loc,'消息模块元素')
        self.click_element(ImLoc.Im_loc,'点击消息模块')
        logger.info("进入消息模块")
    def clickImManageList(self):
        logger.info("点击消息模块消息处理弹窗按钮")
        self.find_element(ImLoc.Im_news_manage_list,'消息处理弹窗按钮')
        self.click_element(ImLoc.Im_news_manage_list,'消息处理弹窗按钮')

        logger.info("消息处理弹窗显示")
    def clickTeamMessage(self,click=1):
        logger.info("查询团队信是否存在")
        self.find_element(ImLoc.Im_team,'团队信消息存在')
        if click != 1:
            logger.info("点击进入消息团队信页面")
            self.click_element(ImLoc.Im_team,'消息团队信')

    def clickNoticeMessage(self,click=1):
        logger.info("互动消息按钮显示")
        self.find_element(ImLoc.Im_notice,"互动消息显示正常")
        if click != 1:
            logger.info("点击进入互动消息页面")
            self.click_element(ImLoc.Im_notice,"互动消息")

    def click1v1Message(self,click=1):
        logger.info("消息列表信息")
        self.find_element(ImLoc.Im_news_lastTime,"1v1消息最后时间")
        if click == 1:
            logger.info("点击最后消息时间")
            self.click_element(ImLoc.Im_news_lastTime,"1v1消息最后时间")
            if self.find_element(ImLoc.Im_news_1v1message_btnReply,"1v1消息预设置按钮"):
                logger.info("进入1v1消息页面")
    def returnBtn(self):
        logger.info("返回")
        #self.find_element(ImLoc.Im_news_1v1message_returnBtn,"返回按钮")

        returnBtn=ImLoc.Im_news_1v1message_returnBtn
        source=self.driver.page_source
        time.sleep(2)
        while True:
            if returnBtn[1] in source:

                self.click_element(ImLoc.Im_news_1v1message_returnBtn,'返回按钮')
                logger.info("循环点击返回按钮，退出到一级页面")
            else:
                logger.info("页面返回到一级页面")
                break







