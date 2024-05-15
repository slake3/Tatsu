import pyautogui
import time
from utils import log_message

def begin():
	pyautogui.click(x=1023, y=626)
	time.sleep(1.5)

def tryLeft(left):
	x = checkOn()
	if x == 0:
		try:
			enemyLocation1 = pyautogui.locateOnScreen(left, confidence =.8)
			center1 = pyautogui.center(enemyLocation1)
			pyautogui.click(center1)
		except:
			log_message("enemy not located")

def tryRight(right):
	x = checkOn()
	if x == 0:
		try:
			enemyLocation2 = pyautogui.locateOnScreen(right, confidence =.8)
			center2 = pyautogui.center(enemyLocation2)
			pyautogui.click(center2)
		except:	
			log_message("enemy not located")
			
def cEnemy(left, right):
	tryLeft(left)
	tryRight(right)
	time.sleep(2)

def sigMove():
	pyautogui.click(x=130, y=858)

def checkBack():
	x = 1
	try: 
		pyautogui.locateOnScreen('back.png', confidence =.9)
		log_message("back button detected")
	except: 
		x = 0
	return x
	
def checkOn():
	try: 
		pyautogui.locateOnScreen('on.png', confidence =.7)
		log_message("battle on detected, in battle")
		x = 1
	except: 
		x = 0
		log_message("battle on NOT detected, NOT in battle")
	return x
	
def back():
	pyautogui.click(x=946, y=1005)
	log_message("back... battle over")
	time.sleep(8)

def exitGlitch():
	close = pyautogui.locateOnScreen('close.png', confidence =.9)
	pyautogui.click(pyautogui.center(close))
	yes = pyautogui.locateOnScreen('yes.png', confidence =.9)
	pyautogui.click(pyautogui.center(yes))
	log_message("...exiting battle glitch")
	back()
	back()
	postMain()
	
	

	


