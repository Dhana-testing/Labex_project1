import pytest
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from gestures import open_all_apps
# from utils.driver_setup import driver_setup

#
# @pytest.fixture(scope="session")
# def driver_setup():
#         caps={
#         "platformName" : "Android",
#         "platformVersion" : "17.0",
#         "deviceName" : "emulator-5554",
#         "automationName" : "UiAutomator2",
#         "app":"/home/user01/Downloads/apk-info-kenumir.apk",
#         # "appPackage": "com.android.deskclock",
#         # "appActivity": "com.android.deskclock.DeskClock",
#         "noReset" : False,
#         "fullReset" : False
#         }
#
#         options = UiAutomator2Options().load_capabilities(caps)
#         driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#         yield driver
#         driver.quit()

@pytest.mark.smoke
def test_app_launch(driver_setup):
        driver = driver_setup
        
        print("Current Activity:", driver.current_activity)
        print("Current Package:", driver.current_package)

        driver.press_keycode(3)

        #Swipe quick settings and click Torch and Bluetooth

        wait = WebDriverWait(driver, 30)
        driver.swipe(500, 50, 500, 1500, 800)
        driver.swipe(500, 500, 500, 1500, 800)


        wait = WebDriverWait(driver, 30)
        bt_element=wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Bluetooth"]')))
        bt_element.click()

        toggle_bt_el=wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'Use Bluetooth')))
        toggle_bt_el.click()
        wait = WebDriverWait(driver, 30)

        driver.press_keycode(3)

        wait = WebDriverWait(driver, 30)

        #Scroll into view Photos and come to home screen

        size = driver.get_window_size()
        open_all_apps(driver, width=size['width'], height=size['height'])
        photos_el = wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Photos"))')))
        photos_el.click()
        driver.implicitly_wait(10)
        driver.press_keycode(3)
        driver.terminate_app

@pytest.mark.smoke
def test_app_scroll(driver_setup):
    driver = driver_setup

    size = driver.get_window_size()
    wait = WebDriverWait(driver, 30)
    open_all_apps(driver, width=size['width'], height=size['height'])
    maps_el=wait.until(EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Maps"))')))
    maps_el.click()

    driver.terminate_app("com.google.android.apps.maps")

    driver.press_keycode(4)

@pytest.mark.smoke
def test_app_settings(driver_setup):
    driver = driver_setup
    wait = WebDriverWait(driver, 10)

    size = driver.get_window_size()
    open_all_apps(driver, width=size['width'], height=size['height'])

    settings_el=wait.until(EC.element_to_be_clickable((AppiumBy.ACCESSIBILITY_ID, 'Settings')))
    settings_el.click()

    netwk_el=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{"Network & internet"}"))'
                                                        )))
    netwk_el.click()

    driver.press_keycode(3)

@pytest.mark.parametrize(
    "app_package,app_activity,scroll_text",
    [
        ("com.google.android.deskclock", "com.android.deskclock.DeskClock","Clock"),
        ("com.android.settings", "com.android.settings.Settings","Settings"),
        ("com.android.chrome", "com.google.android.apps.chrome.Main","Google")
    ]
)

@pytest.mark.smoke
def test_launch_app(driver_setup, app_package, app_activity, scroll_text):
    driver = driver_setup
    driver.activate_app(app_package)
    wait = WebDriverWait(driver, 30)
    element=wait.until(EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
                                f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{scroll_text}"))'
                                )))
    assert element is not None
    driver.press_keycode(4)

@pytest.mark.parametrize(
    "orientation",["LANDSCAPE","PORTRAIT"]
)

@pytest.mark.regression
def test_orientation(driver_setup, orientation):
    driver = driver_setup
    driver.orientation = orientation
    assert driver.orientation == orientation
    wait = WebDriverWait(driver, 30)


@pytest.mark.parametrize("x,y,result",
                         [(2,3,5),(4,5,9),(1,4,3)])
@pytest.mark.regression
def validate_no(driver, x, y, result):
    assert  x+y == result








