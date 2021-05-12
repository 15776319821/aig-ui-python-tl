from pageproject.match_page import MatchPage
from base.base_log import logger
from base.base_action import BaseAction
from elementloc.FancyMe.IM import ImLoc

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






