from gtts  import gTTS
import os
import sys
fh=open("speak.txt","r")
rktText = fh.read().replace("\n","")
language='en'
audio=gTTS(text=rktText,lang=language,slow=False)
audio.save("audio.mp3")
os.system("mv audio.mp3 /sdcard/")
fh.close()



