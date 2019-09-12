from chatterbot import ChatBot

def chat_bot():
	# Create a new instance of a ChatBot
	chatbot = ChatBot(
	    'hacker',
	    read_only=False,
	    storage_adapter='chatterbot.storage.SQLStorageAdapter',
	    logic_adapters=[
		'chatterbot.logic.MathematicalEvaluation',
		#'chatterbot.logic.TimeLogicAdapter',
		'chatterbot.logic.BestMatch'
	    ],
	    database_uri='sqlite:///database.db'
	)
	
	return chatbot

