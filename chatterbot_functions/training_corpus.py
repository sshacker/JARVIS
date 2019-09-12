from chatterbot.trainers import ChatterBotCorpusTrainer

def training_corpus(chatbot):
	trainer = ChatterBotCorpusTrainer(chatbot)

	trainer.train(
	    #USING CHATTERBOT CORPUS ENGLISH DATA
	    "chatterbot.corpus.english"
	    
	    ##SPECIFYING CORPUS SCOPE
	    #"chatterbot.corpus.english.greetings",
	    #"chatterbot.corpus.english.conversations"
	    
	    ##SPECIFYING FILEES PATH TO CORPUS FILES OR DIRECTORIES OF CORPUS FILES 
	    #"./data/greetings_corpus/custom.corpus.json",
	    #"./data/my_corpus/"
	)
	return