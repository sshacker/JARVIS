from jarvis_functions import jar
if __name__ == "__main__":
    while True :
        query = input("\nenter query : ").upper()
        
        #CALL
        jar.jarvis_reply(query)
    
    print("BACK")