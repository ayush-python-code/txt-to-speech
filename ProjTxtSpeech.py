import pyttsx3
print("Welcome to Robot speaker by Ayush singh ")
print("")
engine = pyttsx3.init()
engine.setProperty('rate',150)

text = input("enter anything which you want me to speak: ")
engine.say(text)
    
engine.runAndWait()

