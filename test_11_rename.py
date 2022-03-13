from os import path

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

import os


def get_driver():
    desired_caps = {
        "platformName": "Android",
        "platformVersion": "11",
        "automationName": "uiautomator2",
        "deviceName": "Android Emulator",
        "app": path.abspath("./filemanager.apk"),
    }
    return webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)


def test_11_rename():
    driver = get_driver()

    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located(
                (By.ID, "com.alphainventor.filemanager:id/icon")
            )
        )
        driver.find_element(By.ID, "com.alphainventor.filemanager:id/icon").click()
        
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.ImageView[@content-desc = 'More options']"))
        )
        driver.find_element(
            By.XPATH, "//android.widget.ImageView[@content-desc = 'More options']"
        ).click()



        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='New']"))
        )
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='New']").click()



        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.TextView[@text='Folder']"))
        )
        driver.find_element(By.XPATH, "//android.widget.TextView[@text='Folder']").click()



        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='com.alphainventor.filemanager:id/file_name']"))
        )
        driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='com.alphainventor.filemanager:id/file_name']").send_keys("test_folder")


        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='OK']"))
        )
        driver.find_element(By.XPATH, "//android.widget.Button[@text='OK']").click()
        

        elem = None
        trial = 0

        while True:
            try:
                driver.swipe(470, 1400, 470, 1000, 1)

                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//android.widget.TextView[@resource-id='com.alphainventor.filemanager:id/filename' and @text='test_folder']",
                        )
                    )
                )
                elem = driver.find_element(
                    By.XPATH,
                    "//android.widget.TextView[@resource-id='com.alphainventor.filemanager:id/filename' and @text='test_folder']",
                )

                actions = TouchAction(driver)
                actions.long_press(elem)
                actions.perform()
                WebDriverWait(driver, 10)

                break
            except Exception as e:
                if trial > 7:
                    break
                trial += 1
                print(e)

        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "//android.widget.TextView[@resource-id='com.alphainventor.filemanager:id/text' and @text='Rename']",
                )
            )
        )
        driver.find_element(
            By.XPATH,
            "//android.widget.TextView[@resource-id='com.alphainventor.filemanager:id/text' and @text='Rename']",
        ).click()

        WebDriverWait(driver, 40).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.EditText[@resource-id='com.alphainventor.filemanager:id/file_name']"))
        )
        driver.find_element(By.XPATH, "//android.widget.EditText[@resource-id='com.alphainventor.filemanager:id/file_name']").send_keys("secure_folder")


        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//android.widget.Button[@text='OK']"))
        )
        driver.find_element(By.XPATH, "//android.widget.Button[@text='OK']").click()


        elem = None
        trial = 0

        while True:
            try:
                driver.swipe(470, 1400, 470, 1000, 1)

                WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "//android.widget.TextView[@resource-id='com.alphainventor.filemanager:id/filename' and @text='secure_folder']",
                        )
                    )
                )
                elem = driver.find_element(
                    By.XPATH,
                    "//android.widget.TextView[@resource-id='com.alphainventor.filemanager:id/filename' and @text='secure_folder']",
                )

                break
            except Exception as e:
                if trial > 7:
                    assert False, "'secure_folder' isn't found"
                trial += 1
                print(e)

        WebDriverWait(driver, 6000)

    except Exception as e:
        print(e)
        driver.quit()
