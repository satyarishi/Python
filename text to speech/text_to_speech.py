from gtts import gTTS
from playsound import playsound
audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "hello how u doing. i am sure you are fine",
          lang = language,slow=False)
sp.save(audio)
playsound(audio)
