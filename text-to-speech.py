



#import suprocess to open mp3 audio

import subprocess 

#import gtts convert text to audio file
import gtts


print("welcome to chatbot")



def repeat():
    a=input("ENTER A CHAT:")
#convert to audio file
    t1 = gtts.gTTS(a)  
#save mp3 file
    t1.save("hi.mp3")
#open audio file
    subprocess.call("mpv hi.mp3",shell=True)
 
    if a!="exit":
        repeat()
        
    else:
        print("else")
        

repeat()
    
