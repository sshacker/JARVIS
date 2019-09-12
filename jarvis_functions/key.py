#FOR KEYBOARD EVENTS
import pyautogui as p
import time

# PRESS THE KEYS FOR THE GIVEM QUERY AND WRITE IT 
# KEYBOARD AUTOMATION
def write_query(query):
	"""
		PRESS THE KEYS FOR THE GIVEM QUERY AND WRITE IT
	"""
	time.sleep(1)
	p.typewrite(query.lower(), interval=0.25)
	return
