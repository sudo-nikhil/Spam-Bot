import pyautogui, time #imports pyautogui to automate stuff and time for sleeping
time.sleep(5) #when the control is here, the program waits for 5 secs so that u can
#place ur cursor where ever u like so after 5 secs, the code below starts to run :
script = open("bee.txt", 'r') #opens the file 'bee.txt' and reads it using 'r' parameter
for word in script: #evry sentence in the script, is stored into word
	pyautogui.typewrite(word) #now the word is type-written into the place where ur cursor is
	pyautogui.press("enter") #After it types one sentence, wala! an enter!!
