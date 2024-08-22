import webbrowser as ww

def apps(text):
    text = text.lower()
    
    try:
        if  "youtube" in text:
           ww.open("https://www.youtube.com")
        
        elif  "chat gpt" in text:
            ww.open("https://chat.openai.com/chat")
        
        elif "instagram" in text:
             ww.open("https://www.instagram.com/")

    except Exception as e :
            print("Invalid input")
            print(text)