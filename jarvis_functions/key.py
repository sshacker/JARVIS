#FOR KEYBOARD EVENTS
import pyautogui as p

# PRESS THE KEYS FOR THE GIVEM QUERY AND WRITE IT 
# KEYBOARD AUTOMATION
def write_query(query):
	"""
		PRESS THE KEYS FOR THE GIVEM QUERY AND WRITE IT
	"""
	p.typewrite(query.lower(), interval=0.25)
	return
