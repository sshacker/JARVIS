from jarvis_functions import speaker, key

#FOR KEYBOARD EVENTS
import pyautogui as p

# TO SEARCH THE PROGRAM IN WINDOWS SEARCH-BAR AND OPEN IT
def program(query) :
	"""
			TO SEARCH THE PROGRAM IN WINDOWS SEARCH-BAR AND OPEN IT
	"""
	#LIST OF EACH WORD IN QUERY
	word_list = query.split()
	
	#TO FIND PROGRAM NAME
	i=word_list.index("OPEN")
	query = word_list[i+1]
	
	#TO STRAT SEARCHING
	response = "start searching for "+query
	print(response)
	speaker.speak(response)
	
    #TO OPEN SEARCH BAR FOR SEARCH A PROGRAM
	p.keyDown("win")
	p.press("s")
	p.keyUp("win")
	
	#TO WRITE THE GIVEN QUERY
	key.write_query(query)
	
	#PRESS ENTER 
	p.press("enter")
	
	#OPENING THE PROGRAM
	q = query+" is opening."
	print(q)
	speaker.speak(q)
	
	#do somethings below with opened program
	#...
	return

