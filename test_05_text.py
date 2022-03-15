import pytest 
import logging
from appium import webdriver
from appium.webdriver.webdriver import AppiumBy



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
    def open_List_demo(cls, timeout=10): 
        cls.find_element(AppiumBy.ACCESSIBILITY_ID, "List Demo").click() 
        increment = 0
        while(increment < timeout):
            increment += 1
            
            if increment > 10:
                break
    
    @classmethod
    def my_scroll(cls): 
        cls.find_element(AppiumBy.ACCESSIBILITY_ID, "List Demo")

        cls.scroll(origin_el=AppiumBy.ACCESSIBILITY_ID("Altostratus"), destination_el=AppiumBy.XPATH("Stratus")) 
