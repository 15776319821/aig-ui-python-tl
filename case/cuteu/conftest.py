# -*- coding:utf-8 -*-
import os
import sys
import time

import pytest

from base.base_driver import setdriver
from pageproject.cuteu.loginout.loginout_page import LoginoutPage
sys.path.append(os.getcwd())


# class Testabout():
#     def test_about(self,init_driver):
#         dri=AboutUs(init_driver)
#         time.sleep(2)
#         dri.Us(5)

@pytest.fixture(scope='session')
def init_driver():
    driver = setdriver().runapp()
    # dri = LoginoutPage(driver).loginout()
    yield {'driver':driver}
    # yield {'driver':driver ,'dri':dri}
    dri = LoginoutPage(driver).loginout()
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