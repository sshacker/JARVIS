import webbrowser
from jarvis_functions import speaker

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def youtube(query):
    """
		TASK TO YOUTUBE SEARCH
	"""
    # create a new Chrome session
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    # Navigate to the application home page
    driver.get("http://www.youtube.com")
    
    # get the search textbox
    search_field = driver.find_element_by_name("search_query")
    search_field.clear()

    #user input query
    #user_search_query=input("enter search query :")
    
    to_search=""
    if "PLAY" in query:
        to_search = query.split("PLAY")[1].strip()
    elif "SEARCH" in query:
        to_search = query.split("SEARCH")[1].strip()
    
    # enter search keyword and submit
    search_field.send_keys(to_search)
    search_field.submit()
    
    # get the list of elements which are displayed after the search
    # currently on result page using find_elements_by_class_name method
    lists= driver.find_elements_by_id("video-title")

    # get the number of elements found
    print ("Found " + str(len(lists)) + " searches:")

    current_page_url = driver.current_url
    print(current_page_url)

    i=0
    for listitem in lists:
        item=listitem.get_attribute("innerHTML")
        print (str(i+1)+".",item)
        speaker.speak(item)
        i=i+1
        if(i>=3):
            print("... and many more search results")
            break
            
    info = "which item number would you like to play"
    print(info)
    speaker.speak(info)
    
    i=int(input("enter item number : "))
    lists[i-1].click()
    
    info="start playing..."
    print(info)
    speaker.speak(info)
    
    #player
    q = "'PLAY"
    while q.upper() != "STOP":
        q = input("enter : ")
        if q.upper() == "PLAY" or q.upper() == "PAUSE":
            p=driver.find_elements_by_xpath('//*[@id="player"]')
            p[0].click()
    
    # close the browser window
    driver.quit()
    
    return