import pytest
import logging
from appium import webdriver
from appium.webdriver.webdriver import AppiumBy

logging.basicConfig(format='%(asctime)s %(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.INFO)


class MebaTest04(webdriver):
    desired_capabilites = {
        "platformName": "Android",
        "appium:platformVersion": "9.0",
        "appium:udid": "emulator-5554"
    }

    def __init__(self):
        super().__init__()
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_capabilities)

    def test_04_list_size(self):
        self.app =self.driver.init_driver()
        assert (self) == 7
