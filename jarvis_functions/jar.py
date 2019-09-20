from jarvis_functions import youtube,facebook, program, google 

### A FUNCTION FOR JARVIS RESPONSE 
### TAKE ONE INPUT QUERY AND RETURN NOTHING
def jarvis_reply(query) :
	"""
		TAKE A QUERY AND TO PERFORM A TASK ACCORDING TO QUERY
	"""

	#TASK TO YOUTUBE SEARCH
	if "YOUTUBE" in query:
		return youtube.youtube(query)
        
    #TASK TO FACEBOOK SEARCH
	if "FACEBOOK" in query:
		return facebook.facebook(query)

	#TASK TO GOOGLE SEARCH 
	elif "SEARCH" in query:
		return google.google(query)
    
    #TASK TO OPEN PROGRAM 
	elif "OPEN" in query:
		return program.program(query)
		
	#DO SOMETHINGS FOR OTHER TASKS
	#...
	
	return
