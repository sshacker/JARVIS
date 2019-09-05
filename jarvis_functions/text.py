#FOR CONVERTING THE TEXT-TO-SPEECH
from jarvis_functions import speaker

#FOR TO ACCESS DECLARED VARIABLES
from jarvis_variables import variables

### FOR TAKE INPUT QUERY IN TEXT AND RETURN QUERY
### [ TAKE TEXT INPUT FROM USER AND RETURN INPUT AS QUERY ]
def take_text_command():
    """
        [ TAKE TEXT INPUT FROM USER AND RETURN INPUT AS QUERY ]
    """
    print("\nJARVIS :- ")
    
    #REQUEST USER TO GIVE COMMAND 
    response = "command me sir..."
    print(response)
    speaker.speak(response)

    #TO TAKE INPUT IN QUERY
    query = input("YOU : ")

    #TO CHECK IF TERMINATE COMMAND FOR PROGRAM
    if query.upper().replace(" ","") in variables.terminate :
        response = "HAVE A NICE DAY SIR ! BYE !!"
        print(response)
        speaker.speak(response)
        
        #FOR EXIT THE PROGRAM
        exit()
    
    #RETURN THE INPUT AS QUERY
    return query
