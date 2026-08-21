from appium import webdriver
import pytest
from appium.options.android import UiAutomator2Options

@pytest.fixture(scope="function")
def driver_setup():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Emulator-5554",
        "platformVersion": "17.0",
        # Default app to launch (can be overridden in tests)
        "appPackage": "com.android.settings",
        "appActivity": "com.android.settings.Settings"
    }
    options = UiAutomator2Options().load_capabilities(desired_caps)

    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()