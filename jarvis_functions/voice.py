#SPEECH RECOGNITION BY GOOGLE FOR SPEECH-TO-TEXT 
import speech_recognition as sr
from jarvis_functions import speaker
import variables

### TO TAKE VOICE COMMAND INPUT FROM USER     
def take_voice_command():
    """
        [ TO TAKE VOICE COMMAND INPUT FROM USER ]
    """
    #INSTANCE OF SPEECH RECOGNIZER 
    r = sr.Recognizer()

    #TAKING SPEECH USING MICROPHONE
    with sr.Microphone() as source:
        print("\nlistening...")
        speaker.speak("command me sir...")
        
        #ADJUST FOR BACKGROUND NOISE
        r.adjust_for_ambient_noise(source)
        
        #LISTENING FROM MICROPHONE AS SOURCE
        audio = r.listen(source)
    try:
        #USING GOOGLE SPEECH RECOGNITION CONVERT VOICE-TO-TEXT
        query = r.recognize_google(audio)
        query = query.upper()

        print("\nYOU :- ")
        print(query.lower())
        
        #CLOSE THE PROGRAM IF A TERMINATE COMMAND FROM USER
        if query.replace(" ","") in variables.terminate :
            print("HAVE A NICE DAY SIR ! BYE !!")
            speaker.speak("HAVE A NICE DAY SIR ! BYE !!")
            exit()
        
        #RETURN VOICE INPUT FROM USER IN TEXT FORM    
        return query

    #FOR UN-KNOWN VALUE ERROR OR VOICE COULD NOT DETECTED CLEARLY   
    except sr.UnknownValueError:
        print("\nJARVIS :- ")
        print("I couldn't understand what you said! Would you like to repeat ?")
        speaker.speak("I couldn't understand what you said! Would you like to repeat ?")
        
        #AGAIN CALL FOR VOICE INPUT FROM USER
        return take_voice_command()
    
    #FOR INTERNET CONNECTION ERROR OR REQUEST ERROR FROM SERVER 
    except sr.RequestError as e:
        print("Please check your Internet Connection.")
        print("Could not request results from " + "Google Speech Recognition service; {0}".format(e))
        speaker.speak("Could not request results from " + "Google Speech Recognition service; {0}".format(e))
        
        return take_voice_command()
           
    return
