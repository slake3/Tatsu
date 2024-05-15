import numpy as np
import cv2
import pyautogui
import time
    
def convert_to_gray(image):
    #convert image to array
    screenshot_array = np.array(image)
    #convert to BGR array
    bgr_array = cv2.cvtColor(screenShot_array, cv2.COLOR_RGB2BGR)
    #convert to grayscale image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #convert to grayscale array
    gray_image_array = np.array(gray_image)
    return gray_image_array
    
def log_message(message):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
    print(f"[{timestamp}] {message}")
    
def handle_error(e):
    print(f"An error occured: {e}")
    

    
