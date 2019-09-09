import variables
from jarvis_functions import speaker 

### FOR TAKE INPUT QUERY IN TEXT AND RETURN QUERY
### [ TAKE TEXT INPUT FROM USER AND RETURN INPUT AS QUERY ]
def take_text_command():
    """
        [ TAKE TEXT INPUT FROM USER AND RETURN INPUT AS QUERY ]
    """
    
    #TO TAKE INPUT IN QUERY
    query = input("\nYOU : ")
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
