import pyautogui, time
time.sleep(5)
script = open("bee.txt", 'r')
for word in script:
	pyautogui.typewrite(word) 
	pyautogui.press("enter")