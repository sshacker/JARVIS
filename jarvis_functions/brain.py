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
        if os.path.isfile("bot_brain.brn"):
                kernel.bootstrap(brainFile = "bot_brain.brn")
        
        #FOR CREATING BOT-BRAIN-FILE
        else:
                kernel.bootstrap(learnFiles = "chatbot_files\std-startup.xml", commands = "LOAD AIML B")
                kernel.saveBrain("bot_brain.brn")
        
        #RETURN KERNEL INSTANCE
        return kernel