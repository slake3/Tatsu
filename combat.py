import time
import pyautogui
from actions import cEnemy, sigMove, checkOn, checkBack, exitGlitch
from detection import checkGlitch
from utils import handle_error

def combat(left, right):
	r = checkOn()
	while r !=1:
		cEnemy(left, right)
		r = checkOn()		
	time.sleep(3)
	x = 0
	while x != 1:
		#region =(225, 119, 801, 801)
		sigMove()
		sS = pyautogui.screenshot()
		time.sleep(2.5)
		sS2 = pyautogui.screenshot()
		time.sleep(2.5)
		sS3 = pyautogui.screenshot()
		time.sleep(2.5)
		sS4 = pyautogui.screenshot()
		time.sleep(2.5)
		sS5 = pyautogui.screenshot()
		x = checkBack()
		n = checkGlitch(sS, sS2, sS3, sS4, sS5, .95)
		if n == -1:
		    if x!=1:
			    handle_error("battle not completed")
			    exitGlitch()
	time.sleep(1)
	


