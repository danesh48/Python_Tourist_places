from gtts import gTTS
import os
mytext='Hello Karthiks..!, how are you my boy?   you dirty bitch..'
language='en'
myobj=gTTS(text=mytext, lang=language, slow=False)
myobj.save('voice.mp3')
os.system(' voice.mp3')