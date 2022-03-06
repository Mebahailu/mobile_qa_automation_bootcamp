from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import AppiumBy

desired_capa = {
    "platformName": "Android",
    "appium:platformVersion": "9.0",
    "appium:udid": "emulator-5554"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub/',disired_capa)


driver.find_element(By.XPATH, '').click()