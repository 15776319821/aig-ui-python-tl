import pytest
from base.base_driver import setdriver
import os,sys
sys.path.append(os.getcwd())
import time
from pageproject.aboutus_page import AboutUs
@pytest.fixture(scope='class')
def init_driver():
    driver = setdriver().runapp()
    yield {'driver':driver}
    time.sleep(20)
    driver.quit()