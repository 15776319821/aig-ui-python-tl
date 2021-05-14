# -*- coding:utf-8 -*-
import pytest
from base.base_driver import setdriver
import os,sys
sys.path.append(os.getcwd())
import time
from pageproject.cuteu.aboutus_page import AboutUs

# class Testabout():
#     def test_about(self,init_driver):
#         dri=AboutUs(init_driver)
#         time.sleep(2)
#         dri.Us(5)

@pytest.fixture(scope='class')
def init_driver():
    driver = setdriver().runapp()
    dri = AboutUs(driver).Us(10)
    yield {'driver':driver ,'dri':dri}
    time.sleep(3)
    driver.close_app()
    driver.quit()
# @pytest.fixture(scope='class')
# def init_drivera():
#     driver = desired()
#     match_page = MatchPage(driver)
#     yield {"driver":driver,"match_page":match_page}
#     driver.close_app()
#     driver.quit()

# @pytest.fixture(scope='class')
# def test_about(init_driver):
#     dri=AboutUs(init_driver)
#     time.sleep(2)
#     dri.Us(5)
