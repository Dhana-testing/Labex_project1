from appium import webdriver
# from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait
# from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
# from appium.webdriver.common.multi_action import MultiAction
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction
from gestures import zoom_in, zoom_out, swipe_up, swipe_down, swipe_left, swipe_right, open_all_apps

#
# caps={
# "platformName" : "Android",
# # "platformVersion" : "17.0",
# "deviceName" : "emulator-5554",
# "automationName" : "UiAutomator2",
# "app":"/home/user01/Downloads/apk-info-kenumir.apk",
# # "appPackage": "com.android.deskclock",
# # "appActivity": "com.android.deskclock.DeskClock",
# "noReset" : False,
# "fullReset" : False
# }
#
# options = UiAutomator2Options().load_capabilities(caps)
#
# # Pass options instead of desired_caps
# driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
#
# zoom_in(driver)
# zoom_in(driver)
# # swipe_up(driver)
# zoom_out(driver)
# zoom_out(driver)
# # swipe_right(driver)
#
# driver.press_keycode(3)

# finger = PointerInput(interaction.POINTER_TOUCH, "finger1")
# actions = ActionBuilder(driver, mouse=finger)
#
# actions.pointer_action.move_to_location(500, 1000)
# actions.pointer_action.pointer_down()
# actions.pointer_action.pause(2)
# actions.pointer_action.pointer_up()
# actions.perform()

# driver.press_keycode(3)
#
# wait = WebDriverWait(driver, 20)
# maps_element=wait.until(EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "Maps")))
# maps_element.click()
#
# webdriverwait = WebDriverWait(driver, 30)

# Create ActionBuilder
# actions = ActionBuilder(driver)
#
# size = driver.get_window_size()
# #Swipe up
# start_x = size["width"] // 2
# start_y = int(size["height"] * 0.80)
#
# end_x = start_x
# end_y = int(size["height"] * 0.20)
#
# swipe(driver,    start_x,    start_y,    end_x,    end_y,    duration=800)
#
# #swipe down
# size = driver.get_window_size()
#
# start_x = size["width"] // 2
# start_y = int(size["height"] * 0.20)
#
# end_x = start_x
# end_y = int(size["height"] * 0.80)
#
# swipe(driver, start_x, start_y, end_x, end_y)