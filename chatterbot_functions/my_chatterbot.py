from chatterbot_functions import chat_bot
from chatterbot_functions import training_corpus
from chatterbot_functions import training_list

def my_chatterbot():        
    #CREATE A NEW INSTANCE OF A CHATBOT
    chatbot = chat_bot.chat_bot()

    #TRAINING CHATBOT USING CHATTERBOT CORPUS ENGLISH DATA
    training_corpus.training_corpus(chatbot)

    #TRAINING CHATBOT USING  OWN LIST DATA 
    training_list.training_list(chatbot)

    print('Type something to begin...')

    # THE FOLLOWING LOOP WILL EXECUTE EACH TIME THE USER ENTERS INPUT
    while True:
        try:
            user_input = input("enter :")
            bot_response = chatbot.get_response(user_input)
            print(bot_response)

        #PRESS CTRL-C OR CTRL-D ON THE KEYBOARD TO EXIT
        except (KeyboardInterrupt, EOFError, SystemExit):
            break
    
    return 