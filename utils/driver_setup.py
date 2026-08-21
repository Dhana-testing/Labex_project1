from appium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver_setup():
    desired_caps = {
        "platformName": "Android",
        "automationName": "UiAutomator2",
        "deviceName": "Emulator-5554",
        "platformVersion": "11.0",
        # Default app to launch (can be overridden in tests)
        "appPackage": "com.android.settings",
        "appActivity": "com.android.settings.Settings"
    }
    options = UiAutomator2Options().load_capabilities(caps)

    driver = webdriver.Remote("http://129.0.0.1:4723/wd/hub", options=options)
    yield driver
    driver.quit()