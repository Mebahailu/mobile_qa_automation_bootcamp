from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.webdriver import AppiumBy

desired_capa = {
    "platformName": "Android",
    "appium:platformVersion": "9.0",
    "appium:udid": "emulator-5554"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub/',disired_capa)


def test_08_scroll(driver):
    self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'List Demo').click()
    self.driver.implicitly_wait(1)
    actions = ActionChains(self.driver)
    actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    actions.w3c_actions.pointer_action.move_to_location(570, 1344)
    actions.w3c_actions.pointer_action.pointer_down()
    actions.w3c_actions.pointer_action.move_to_location(579, 512)
    actions.w3c_actions.pointer_action.release()
    actions.perform()
    log.info("Check last item is available")
    return self.driver.find_element(AppiumBy.ACCESSIBILITY_ID, 'Stratus')
