import pyttsx3
text_speech = pyttsx3.init()
ola = 'Olá, aqui é o gugu'
text_speech.say(ola)
text_speech.runAndWait()
'''ola = 'O que você quer ouvir, gugu?'
text_speech.say(ola)
text_speech.runAndWait()
seila = input('O que você quer ouvir? ')
seila = 'Olá'
text_speech.say(seila)
text_speech.runAndWait()'''



# Import the required module for text
# to speech conversion
'''import gtts
This module is imported so that we can
play the converted audio
import os

The text that you want to convert to audio
mytext = 'Welcome to geeksforgeeks!'
Language in which you want to convert
language = 'en'
Passing the text and language to the engine,
here we have marked slow=False. Which tells
the module that the converted audio should
have a high speed
myobj = gTTS(text=mytext, lang=language, slow=True)

Saving the converted audio in a mp3 file named
welcome
myobj.save("welcome.mp3")

Playing the converted file
os.system("mpg321 welcome.mp3")
tts = gTTS('hello')'''
import gtts
from gtts import lang
print(lang.tts_langs())
# 'pt': 'Portuguese'
from gtts import gTTS
from pygame import mixer
import time
# Create the text
text = "Hello World!"
tts = gTTS(text, slow=False)
# Save the audio in a mp3 file
tts.save('hello.mp3')
# Play the audio
mixer.init()
mixer.music.load("hello.mp3")
mixer.music.play()
# Wait for the audio to be played
time.sleep(2)