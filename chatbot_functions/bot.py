#FOR AIML AND KERNEL OBJECT
import aiml

from jarvis_functions import speaker

### A FUNCTION FOR CHAT-BOT RESPONSE FROM ALICE AIML FILES
### TAKE TwO INPUT QUERY AND KERNEL INSTANCE AND RETURN NOTHING
def chat_bot_reply(query, kernel):
    """
        [ TAKE TWO INPUT QUERY AND KERNEL INSTANCE AND RETURN NOTHING ]
    """
    #GET REPLY FOR QUERY FROM AIML FILES
    bot_reply = kernel.respond(query.upper())

    print("CHAT BOT :- ")
    print(bot_reply)
    speaker.speak(bot_reply)

    return
