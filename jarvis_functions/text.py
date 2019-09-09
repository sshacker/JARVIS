from jarvis_functions import speaker
import variables

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
    query = query.upper()
    
    #TO CHECK IF TERMINATE COMMAND FOR PROGRAM
    if query.replace(" ","") in variables.terminate :
        response = "HAVE A NICE DAY SIR ! BYE !!"
        print(response)
        speaker.speak(response)
        
        #FOR EXIT THE PROGRAM
        exit()
    
    #RETURN THE INPUT AS QUERY
    return query
