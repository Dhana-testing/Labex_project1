def zoom_in(driver, left=100, top=400, width=800, height=800, percent=0.75):
    driver.execute_script("mobile: pinchOpenGesture", {
        "left": left, "top": top, "width": width, "height": height, "percent": percent
    })

def zoom_out(driver, left=100, top=400, width=800, height=800, percent=0.75):
    driver.execute_script("mobile: pinchCloseGesture", {
        "left": left, "top": top, "width": width, "height": height, "percent": percent
    })

def swipe_up(driver, left=100, top=400, width=800, height=800, percent=0.75):
    driver.execute_script("mobile: swipeGesture", {
        "left": left, "top": top, "width": width, "height": height,
        "direction": "up", "percent": percent
    })

def swipe_down(driver, left=100, top=400, width=800, height=800, percent=0.75):
    driver.execute_script("mobile: swipeGesture", {
        "left": left, "top": top, "width": width, "height": height,
        "direction": "down", "percent": percent
    })

def swipe_left(driver, left=100, top=400, width=800, height=800, percent=0.75):
    driver.execute_script("mobile: swipeGesture", {
        "left": left, "top": top, "width": width, "height": height,
        "direction": "left", "percent": percent
    })

def swipe_right(driver, left=100, top=400, width=800, height=800, percent=0.75):
    driver.execute_script("mobile: swipeGesture", {
        "left": left, "top": top, "width": width, "height": height,
        "direction": "right", "percent": percent
    })

def open_all_apps(driver, width, height):
    """
    Swipe up from bottom center to open All Apps page.
    """
    start_x = width // 2
    start_y = int(height * 0.92)  # near bottom
    end_x = width // 2
    end_y = int(height * 0.33)  # about one-third from top

    driver.execute_script("mobile: swipeGesture", {
        "left": 0,
        "top": 0,
        "width": width,
        "height": height,
        "direction": "up",
        "percent": 0.75
    })