import pytest
import allure
from appium import webdriver
from selenium.webdriver.common.actions import mouse_button
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from appium.options.android import UiAutomator2Options
from gestures import open_all_apps
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput


# @pytest.fixture(scope="session")
# def driver_setup():
#     caps = {
#         "platformName": "Android",
#         "platformVersion": "17.0",
#         "deviceName": "emulator-5554",
#         "automationName": "UiAutomator2",
#         # "app": "/home/user01/Downloads/apk-info-kenumir.apk",
#         "apppackageName": "com.android.chrome",
#         "appActivity": "com.android.chrome.Main",
#         "noReset": False,
#         "fullReset": False
#     }
#     options = UiAutomator2Options().load_capabilities(caps)
#     driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#     yield driver
#     driver.quit()

@allure.feature("Mobile App")
@allure.story("App Launch")
@allure.severity(allure.severity_level.CRITICAL)
def test_app_launch(driver_setup):
    driver = driver_setup
    driver.press_keycode(4)
    finger=PointerInput("touch","finger")
    actions = ActionBuilder(driver,mouse=finger)
    actions.pointer_action.move_to_location(670,2000)
    actions.pointer_action.pointer_down()
    actions.pointer_action.pause(4)
    actions.pointer_action.pointer_up()
    actions.perform()
    wait=WebDriverWait(driver, 10)
    chrome_app_info_el=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("App info")')))
    chrome_app_info_el.click()
    allure.attach(driver.page_source, name="Page Source", attachment_type=allure.attachment_type.TEXT)
    assert "Chrome" in driver.page_source

    wait=WebDriverWait(driver, 10)

    
    #
    # driver.press_keycode(3)
    #
    # # Scroll into view Photos and come to home screen
    # driver.swipe(500, 1500, 500, 100, 800)
    # photos_el = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
    #     'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Photos"))')))
    # photos_el.click()
    #
    # driver.terminate_app("com.google.android.apps.photos")
    #
    # size = driver.get_window_size()
    # open_all_apps(driver, width=size['width'], height=size['height'])
    # maps_el = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
    #     'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Maps"))')))
    # maps_el.click()
    #
    # driver.press_keycode(4)
    #
    # # Scroll to view settings and click Network and internet
    #
    # size = driver.get_window_size()
    # open_all_apps(driver, width=size['width'], height=size['height'])
    # settings_el = wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Settings")))
    # settings_el.click()
    #
    # netwk_el = wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Network & internet")')))
    # netwk_el.click()
    #
    # driver.press_keycode(3)

