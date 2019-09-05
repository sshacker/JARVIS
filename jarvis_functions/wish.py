import datetime
from jarvis_functions import speaker

#A FUNCTION TO WISH THE USER ON START
def wish_me(user):
    hour = int(datetime.datetime.now().hour)
    print("\nJARVIS :- ")
    response = "WELCOME : " + user.upper() 
    print(response)
    speaker.speak(response)

    if hour>=0 and hour<12:
        response = "good morning !"
        print(response)
        speaker.speak(response)

    elif hour>=12 and hour<18:
        response = "good afternoon !"
        print(response)
        speaker.speak(response)
    
    else:
        response = "good evening !"
        print(response)
        speaker.speak(response)
    
    response = "I am JARVIS sir. How may I help you ?"
    print(response)
    speaker.speak(response)
    return
