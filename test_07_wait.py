import pytest 
import logging
from appium import webdriver
from appium.webdriver.webdriver import AppiumBy



logging.basicConfig(format='%(asctime)s %(message)s',filemode='w')  
logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Automation(webdriver):
    desired_capabilites = {
    "platformName": "Android",
    "appium:platformVersion": "9.0",
    "appium:udid": "emulator-5554"
        }

    def __init__(self):
        super().__init__()
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", self.desired_capabilities)

        
    @classmethod
    def open_app(cls,expected):
        
            
        size = cls.driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="TheApp"][1]').size()  
        

        logger.info(f'List size: {size} expected:{expected}')

    @classmethod
    def get_element_by_text(cls, text): 
        exist = False
        try:
            cls.driver.find_element_by_text(f"{text}")
            exist = True
            return exist
        except Exception as error:
            exist = False
            return exist
