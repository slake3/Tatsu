from skimage.metrics import structural_similarity as ssim
from utils import convert_to_gray, log_message, handle_error
import matplotlib.pyplot as plt
import numpy as np
import cv2
import pyautogui
import time
import pyscreeze

def checkGlitch(screenShot, screenShot2, screenShot3, screenShot4, screenShot5, tolerance):
	x = 0
	try:
	        #take final screenshot
        	screenShot6 = pyautogui.screenshot()
        	#convert screenshots to gray image arrays
        	gray_image1_array = convert_to_gray(screenShot)
        	gray_image2_array = convert_to_gray(screenShot2)
        	gray_image3_array = convert_to_gray(screenShot3)
        	gray_image4_array = convert_to_gray(screenShot4)
        	gray_image5_array = convert_to_gray(screenShot5)
        	gray_image6_array = convert_to_gray(screenShot6)
        	#set win_size to odd within value limits
        	win_size = min(gray_image1_array.shape[:2])
        	win_size = win_size if win_size % 2 == 1 else win_size -1
        	#calculate ssims
        	similarity_index1 = ssim(gray_image1_array, gray_image2_array, win_size=win_size)
        	similarity_index2 = ssim(gray_image2_array, gray_image3_array, win_size=win_size)
        	similarity_index3 = ssim(gray_image3_array, gray_image4_array, win_size=win_size)
        	similarity_index4 = ssim(gray_image4_array, gray_image5_array, win_size=win_size)
        	similarity_index5 = ssim(gray_image5_array, gray_image6_array, win_size=win_size)
        	#test ssims
       		if similarity_index1 < tolerance:
       		    log_message("ssim comparison 1 failed")
       		    if similarity_index2 < tolerance:
       		        log_message("ssim comparison 2 failed")
       		        if similarity_index3 < tolerance:
       		            log_message("ssim comparison 3 failed")
       		            if similarity_index4 < tolerance:
       		                log_message("ssim comparison 4 failed")
       		                if similarity_index5 < tolerance:
       		                    log_message("ssim comparison 5 failed...")
       		                    x = -1
        	else:
            		x = 0
	except ValueError as e:
        	log_message(f"ValueError: {e}")
        	log_message(f"ScreenShot array shape: {gray_image1_array.shape}")
        	log_message(f"ScreenShot2 array shape: {gray_image2_array.shape}")
        	log_message(f"ScreenShot3 array shape: {gray_image3_array.shape}")
        	log_message(f"ScreenShot4 array shape: {gray_image4_array.shape}")
        	log_message(f"ScreenShot5 array shape: {gray_image5_array.shape}")
        	log_message(f"ScreenShot6 array shape: {gray_image6_array.shape}")
	return x
