import os,sys
sys.path.append(os.getcwd())
from pageproject.match_page import MatchPage
from base.base_log import logger

class TestStartApp():
    def test_start(self,init_driver):
        logger.info("执行前")
        pass