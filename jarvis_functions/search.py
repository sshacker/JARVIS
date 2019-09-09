import webbrowser
from jarvis_functions import speaker

def search(query):
    """
        TASK TO GOOGLE SEARCH 
    """
    google_url = "https://www.google.com/search?q="
    
    #TO EXTRACT THE STRING TO WE SEARCH
    to_search = query.split("SEARCH")[1].strip()
    word_list = to_search.lower().split()

    #JOIN THE STRING TO FORM COMPLETE URL FOR GOOGLE CHROME BROWSER
    to_search = "+".join(word_list)
    url = google_url + to_search

    #OPEN DEFAULT BROWSER
    webbrowser.open(url)
    
    q="start searching form internet for your query "
    print(q)
    speaker.speak(q)
    
    return