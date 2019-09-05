#VARIABLES : FOR TO ACCESS DECLARED VARIABLES
#BOT : FOR CHAT BAT REPLY FROM FROM AIML FILES
#BRAIN : FOR KERNEL BRAIN-FILE USING AIML FILES
#SPEAKER : FOR CONVERTING THE TEXT-TO-SPEECH
#TEXT : FOR TAKE INPUT QUERY IN TEXT AND RETURN QUERY
#WISH :FOR INITIALLY WISH TO THE USER

from jarvis_variables import variables

from jarvis_functions import bot
from jarvis_functions import brain
from jarvis_functions import speaker
from jarvis_functions import text
from jarvis_functions import wish


##################################################
### MAIN START POINT OF THE SOFTWARE (PROGRAM) ###
##################################################

if __name__ == "__main__" :
    #START RUNNING
    query = "\n:: WAIT WHILE LOADING REQUIRED FILES ::\n"
    print(query)
    speaker.speak(query)

    #BRAIN FILE
    kernel = brain.chat_bot_brain()

    #TO GET USER NAME
    query = "Please enter your name : "
    speaker.speak(query)
    user = input(query)
    
    #ON START WISH TO USER
    wish.wish_me(user)

    #NOW READY TO TAKE A COMMMAN FROM USER
    print("\n:: Now J.A.R.V.I.S Ready ::\n")
    command_type = input("Command Type [ text OR voice ] : ")
    print(command_type)

    #COMMAND TYPE CHECKING IF TEXT OR VOICE TYPE
    if command_type.lower() == "text":
        #FOR TEXT COMMAND
        while True:
            #TO TAKE THE INPUT FOR QUERY IN TEXT FORM
            query = text.take_text_command()
            
            #TO REPLY THE QUERY FROM CHAT-BOT
            bot.chat_bot_reply(query, kernel)
