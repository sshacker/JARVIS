from chatbot_functions import *
from jarvis_functions import *
import time

####################################################
### MAIN START POINT OF THE SOFTWARE (PROGRAM) ###
####################################################

def main() :
    #TO GET USER NAME
    query = "PLEASE ENTER YOUR NAME : "
    print(query)
    speaker.speak(query)
    user = input()
    
    #WELCOME TO USER
    response="WELCOME "+user.upper()
    print(response)
    speaker.speak(response)
    
    #SELECT ASSISTANCE TYPE 
    info = "PLEASE SELECT YOUR ASSISTANT TYPE"
    print(info)
    print("1. CHAT BOT")
    print("2. JARVIS")
    speaker.speak(info)
    i = int(input("enter : "))

    #########################################
    ###   FOR CHAT BOT
    ##########################################
    if i==1:
        info = "WAIT WHILE LOADING REQUIRED FILES"
        print("\n:: "+info+" ::\n")
        speaker.speak(info)
        
        #BRAIN FILE
        kernel = brain.chat_bot_brain()

        #NOW READY TO TAKE A COMMMAN FROM USER
        info="Now CHAT BOT Ready"
        print("\n:: "+info+" ::\n")
        speaker.speak(info)
        info="Hello sir how i can help you?"
        print("CHAT BOT :\nHello sir how i can help you?")
        speaker.speak(info)

        #FOR TEXT COMMAND
        while True:
            #TO TAKE THE INPUT FOR QUERY IN TEXT FORM
            query = chat.take_text_command()
            
            #TO REPLY THE QUERY FROM CHAT-BOT
            bot.chat_bot_reply(query, kernel)

    #########################################
    ###   FOR JARVIS
    #########################################
    else:
        #ON START WISH TO USER
        wish.wish_me(user)
        
        #TAKE COMMAND TYPE
        info="SELECT COMMAND TYPE"
        print(info)
        speaker.speak(info)
        print("1. TEXT")
        print("2. VOICE")
        time.sleep(1)
        i = int(input("enter : "))

        #COMMAND TYPE IF TEXT
        if i == 1:
            while True:
                #TO TAKE THE INPUT FOR QUERY IN TEXT FORM
                query = text.take_text_command()

                #TO REPLY THE QUERY FROM JARVIS
                jar.jarvis_reply(query)

        #COMMAND TYPE IF VOICE
        else :
            while True:
                #TO TAKE THE INPUT FOR QUERY IN TEXT FORM
                query = voice.take_voice_command()

                #TO REPLY THE QUERY FROM JARVIS
                jar.jarvis_reply(query)
    return 0

if __name__ == "__main__":
        main()