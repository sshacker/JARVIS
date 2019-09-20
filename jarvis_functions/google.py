import webbrowser
from jarvis_functions import speaker

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def google(query):
    """
        TASK TO GOOGLE SEARCH 
    """
    # create a new Firefox session
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    
    # Navigate to the application home page
    driver.get("http://www.google.com")
    
    # get the search textbox
    search_field = driver.find_element_by_name("q")
    search_field.clear()
    
    to_search = query.split("SEARCH")[1].strip()
    
    #user input query
    #user_search_query=input("enter search query :")

    # enter search keyword and submit
    search_field.send_keys(to_search)
    search_field.submit()
    
    # get the list of elements which are displayed after the search
    # currently on result page using find_elements_by_class_name method
    lists= driver.find_elements_by_class_name("ellip")

    # get the number of elements found
    print ("Found " + str(len(lists)) + " searches:")

    # iterate through each element and print the text that is
    # name of the search

    i=0
    for listitem in lists:
        item = listitem.get_attribute("innerHTML")
        print (str(i+1)+".",item)
        speaker.speak(item)
        i=i+1
        if(i>=5):
            print(".... and many more search results")
            break

            
    info = "which item number would you like to open"
    print(info)
    speaker.speak(info)
    
    i=int(input("enter item number : "))
    lists[i-1].click()
    
    info="start opening..."
    print(info)
    speaker.speak(info)
    
    input("HALT")
    # close the browser window
    driver.quit()
 
    return