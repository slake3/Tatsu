from combat import combat
from actions import begin, back, postMain

def main():
	begin()
	x = 0
	while x < 100:
		combat('leftShot.png', 'rightShot.png')
		back()
		x+=1
def postMain():
	print("finding new enemy")
	pyautogui.press('s', presses = 3)
	pyautogui.press('d', presses = 3)
	x = 0
	while x <100:
		combat('leftShot2.png', 'rightShot2.png')
		back()
		x+=1
