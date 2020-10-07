import pyttsx3

engine = pyttsx3.init('sapi5')
engine.setProperty("rate", 178)
engine.say("vikram singh")
engine.runAndWait()
