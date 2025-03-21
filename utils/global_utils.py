import os
import time
import cv2
import logging
import subprocess
import config
from datetime import timedelta
from timeit import default_timer as timer

import random

# Take screenshot and return it in cv2 format
def take_screenshot(name):
    subprocess.call(
        ["adb", "-s", config.global_adb_port, "exec-out", "screencap", "-p", ">", config.project_path+"\\"+name], stdout=subprocess.PIPE, shell=True)
    return cv2.imread(config.project_path+'\\'+name)


# Search if the haystack image is a subimage of the current image
def search(haystack_image_path, screenshot, precision=0):
    method = cv2.TM_SQDIFF_NORMED
    haystack_image = cv2.imread(haystack_image_path)
    result = cv2.matchTemplate(haystack_image, screenshot, method)
    min_val, _, min_loc, _ = cv2.minMaxLoc(result)
    mp_x, mp_y = min_loc
    threshold = 0.14
    if precision:
        threshold = 0.03
    if min_val < threshold:
        return [1, [mp_x, mp_y], haystack_image]
    else:
        return [0, [0, 0], None]


# Checks if a haystack image from a folder exists in the screenshot
def search_in_folder(folder_path, screenshot):
    for card_haystack in os.listdir(folder_path):
        searched_image = search(folder_path+"\\"+card_haystack, screenshot)
        if searched_image[0] == 1:
            return searched_image
    return [0]


# Click a position
def click(x, y):
    x += random.randint(-5,5)
    y += random.randint(-3,3)
    
    subprocess.call(
        ["adb", "-s", config.global_adb_port, "shell", "input", "tap", str(x), str(y)], stdout=subprocess.PIPE, shell=True)


# Click a position with a tuple
def click(position):
    subprocess.call(
        ["adb", "-s", config.global_adb_port, "shell", "input", "tap", str(position[0] + random.randint(-5,5) ), 
                                                    str(position[1] + random.randint(-5,5))], stdout=subprocess.PIPE, shell=True)


# Swipe from a position a to a position b
def drag(position_1, position_2):
    subprocess.call(
        ["adb", "-s", config.global_adb_port, "shell", "input", "touchscreen", "swipe", str(position_1[0]), str(position_1[1]), 
         str(position_2[0] + random.randint(-20,20)), str(position_2[1]+ random.randint(-20,20)), 
         str(500 + random.randint(-100,100) )], stdout=subprocess.PIPE, shell=True)


# Find and click if found a subimage
# Returns 1 if it found the image and clicked on it, otherwise 0
def find_and_click(haystack_image_path, screenshot):
    search_haystack_image = search(haystack_image_path, screenshot)
    if search_haystack_image[0] == 1:
        click(search_haystack_image[1])
        logging.info("* find img :" + str(haystack_image_path))
        return 1
    else:
        return 0


# Wait until the image is gone
def wait_until_gone(haystack_image_path):
    while search(haystack_image_path)[0]:
        time.sleep(1)


# Wait until the image is found
def wait_until_found(haystack_image_path, screenshot):
    while not search(haystack_image_path, screenshot, False)[0]:
        time.sleep(1)


# Draw a rectangle to the image
def draw(screenshot, search_haystack_image, name, colors):
    if search_haystack_image[0] == 1:
        # Get haystack size
        trows, tcols = search_haystack_image[2].shape[:2]

        # Text settings
        font = cv2.FONT_HERSHEY_SIMPLEX
        x = search_haystack_image[1][0]
        y = search_haystack_image[1][1]
        org = (x, y+trows+25)
        colors = (colors[0], colors[1], colors[2])
        fontScale = 0.7

        # Draw border text
        screenshot = cv2.putText(
            screenshot, name, org, font, fontScale, (0, 0, 0), 10, cv2.LINE_AA)

        # Draw inner text
        screenshot = cv2.putText(
            screenshot, name, org, font, fontScale, colors, 4, cv2.LINE_AA)

        # Draw rectangle
        screenshot = cv2.rectangle(
            screenshot, (x, y), (x+tcols, y+trows), colors, 2)

        return screenshot
    else:
        return screenshot


# Start the timer for the elapsed time
def start_timer():
    return timer()


# End the timer for the elapsed time
def end_timer():
    return timer()


# Log the time elapsed of the function
def log_time_elapsed(function, time):
    logging.info("["+function+"] Time elapsed: " +
                 str(timedelta(seconds=time)))
