from jarvis_variables import variables

from jarvis_functions import speaker
from jarvis_functions import wish

if __name__ == "__main__" :
    query = "\n:: WAIT WHILE LOADING REQUIRED FILES ::\n"
    print(query)
    speaker.speak(query)

    query = "Please enter your name : "
    speaker.speak(query)
    user = input(query)
    
    # ON START WISH TO USER
    wish.wish_me(user)