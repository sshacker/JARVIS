from chatterbot.trainers import ListTrainer

def training_list(chatbot):
	trainer = ListTrainer(chatbot)
	conversation = [
	    'How are you?',
	    'I am good.',
	    'That is good to hear.',
	    'Thank you',
	    'You are welcome.',
	]
	trainer.train(conversation)

	trainer.train([
	    "Hi there!",
	    "Hello",
	])

	trainer.train([
	    "Greetings!",
	    "Hello",
	])
	
	return