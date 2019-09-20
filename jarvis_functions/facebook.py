from jarvis_functions import speaker
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import getpass

def facebook(query):
    
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()
    
    driver.get("http://www.facebook.com")
    
    info="Enter your e-mail"
    print(info)
    speaker.speak(info)
    user_name = input("email : ")
    
    info="Enter your password"
    print(info)
    speaker.speak(info)
    pwd = getpass.getpass("password : ")

    assert "Facebook" in driver.title

    elem = driver.find_element_by_id("email")
    elem.send_keys(user_name)

    elem = driver.find_element_by_id("pass")
    elem.send_keys(pwd)

    elem.send_keys(Keys.RETURN)
    
    info="Your facebook account is opening."
    print(info)
    speaker.speak(info)
    
    input("HALT")
    # close the browser window
    driver.close()
    return