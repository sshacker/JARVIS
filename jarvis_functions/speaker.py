#FOR OFFLINE TEXT-TO-SPEECH
import pyttsx3

#FOR ONLINE TEXT-TO-SPEECH
from gtts import gTTS
import os

from jarvis_functions import speaker
from jarvis_variables import variables

#PYTTSX3 INITIALIZATIONS
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

#A FUNCTION IF ONLINE : SPEAK FOR JARVIS USING GOOGLE gTTT
def online_gtts_speak(jarvis_speech):
    """
        [ A FUNCTION IF ONLINE : SPEAK FOR JARVIS USING GOOGLE gTTT ]
    """
    tts = gTTS(text=jarvis_speech, lang='en')
    tts.save("audio.mp3")
    os.system("audio.mp3")
    return

#A FUNCTION IF OFFLINE : SPEAK FOR JARVIS USING PYTTSX3
def offline_pyttsx3_speak(jarvis_speech):
    """
        [ A FUNCTION IF OFFLINE : SPEAK FOR JARVIS USING PYTTSX3 ]
    """
    engine.say(jarvis_speech)
    engine.runAndWait()
    return

#A MAIN SPEAK FUNCTION
def speak(jarvis_speech):
    """
        [ A MAIN SPEAK FUNCTION ]
    """
    #IF OFFLINE
    if variables.command_mode == "offline" :
        offline_pyttsx3_speak(jarvis_speech)
    
    #IF ONLINE
    else:
        online_gtts_speak(jarvis_speech)
    return