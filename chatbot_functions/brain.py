#FOR AIML AND KERNEL OBJECT
import aiml
import os

#CHAT-BOT BRAIN FILE READING OR CREATING FROM AIML FILES
def chat_bot_brain() :
        """
                [ CHAT-BOT BOT_BRAIN.BRN FILE ]
        """
        #AIML KERNEL INSTANCE
        kernel = aiml.Kernel()

        #FOR READ BOT-BRAIN-FILE
        if os.path.isfile("chatbot_functions/bot_brain.brn"):
                kernel.bootstrap(brainFile = "chatbot_functions\\bot_brain.brn")
        
        #FOR CREATING BOT-BRAIN-FILE
        else:
                kernel.bootstrap(learnFiles = "chatbot_functions\std-startup.xml", commands = "LOAD AIML B")
                kernel.saveBrain("chatbot_functions\\bot_brain.brn")
        
        #RETURN KERNEL INSTANCE
        return kernel