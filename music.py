import webbrowser



def songs(text):
     
    if ("mana apna" in text) == True  :
        webbrowser.open("https://youtube.com/shorts/GxSObCAzXEE?si=5xuy8vLUd4pIEiSR")#Mana Apna

    elif ("hanuman chalisa" in text) == True :
        webbrowser.open("https://youtu.be/ENzldKJRmf8?si=ARwUxoCQ94c1m1bx") #Hanuman Chalisa
    
    elif ("maruti stotra" in text) == True :
        webbrowser.open("https://youtu.be/1qywgxZ9A58?si=B97aFkVXBcMb-U8f") #Maruti Stotra

    elif ("chammak challo" in text) == True :
        webbrowser.open("https://youtube.com/shorts/BtO_67ho17U?si=YO5Apz6If_pTMowI") #chamak challo
 

    else :
        print(text)
    



