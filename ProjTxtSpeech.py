import pyttsx3
# initialize Text-to-speech engine
print("Welcome to Robot speaker by Ayush singh ")
print("")
engine = pyttsx3.init()
engine.setProperty('rate',150)
# convert this text to speech

text = input("enter anything which you want me to speak: ")
engine.say(text)
    
engine.runAndWait()
