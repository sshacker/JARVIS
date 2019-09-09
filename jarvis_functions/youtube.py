import webbrowser
from jarvis_functions import speaker

def youtube(query):
    """
		TASK TO YOUTUBE SEARCH
	"""
    youtube_url="https://www.youtube.com/results?search_query="
    if "PLAY" in query:
        #TO EXTRACT THE STRING TO WE SEARCH
        to_search = query.split("PLAY")[1].strip()
        word_list = to_search.lower().split()

        #JOIN THE STRING TO FORM COMPLETE URL FOR YOUTUBE SEARCH
        to_search = "+".join(word_list)
        url=youtube_url+to_search

        #OPEN DEFAULT BROWSER
        webbrowser.open(url)

    elif "SEARCH" in query:
        #TO EXTRACT THE STRING TO WE SEARCH
        to_search = query.split("SEARCH")[1].strip()
        word_list = to_search.lower().split()

        #JOIN THE STRING TO FORM COMPLETE URL FOR YOUTUBE SEARCH
        to_search = "+".join(word_list)
        url= youtube_url + query

        #OPEN DEFAULT BROWSER
        webbrowser.open(url)
    
    else :
        #OPEN DEFAULT BROWSER
        webbrowser.open(youtube_url)
    
    q="start searching form youtube for your query "
    print(q)
    speaker.speak(q)
    
    return