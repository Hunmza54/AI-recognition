from neuralintents import GenericAssistant
import speech_recognition
import pyttsx3 as talking
import nltk
import sys

nltk.download('omw-1.4')

recognizer = speech_recognition.Recognizer()

myfriend = talking.init()
myfriend.setProperty('rate',150) #sets the speed AI speaks in 

about_friends = {'fun','Helpful'}

def add_friend():
    global recognizer
    myfriend.say("What is the name of your new friend?")
    myfriend.runAndWait()
    done = False
    
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recognizer.listen(mic)
                note = recognizer.recognize_google(audio)
                note = note.lower()
                
                myfriend.say("choose a file name")
                myfriend.runAndWait()
                recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recognizer.listen(mic)
                filename = recognizer.recognize_google(audio)
                filename.lower()
                
            with open(filename, 'w') as f:
                f.write(note)
                done = True
                myfriend.say(f"I have added the friend {filename}")
                myfriend.runAndWait()
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            myfriend.say("I dont understant")
            myfriend.runAndWait()
            
def about_friend():
    global recognizer
    myfriend.say("Things you want to add about this friend?")
    myfriend.runAndWait()
    done = False
    
    while not done:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration = 0.2)
                audio = recognizer.listen(mic)
                about_them= recognizer.recognize_google(audio)
                about_them= about_them.lower()
                about_friends.append(about_them)
                
                done = True
                
                myfriend.say(f"I added a trait {about_them}")
                myfriend.runAndWaut()
                
        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            myfriend.say("I dont understant")
            myfriend.runAndWait()
            
def hello():
    myfriend.say("Hello, What can I do for you?")
    myfriend.runAndWait()
    

def quit():
    myfriend.say("Bye")
    myfriend.runAndWait()
    sys.exit(0)
    
    
mapping = { 'greeting': hello,
            'add_friend':add_friend,
           'about_friend':about_friend,
           'quit':quit
           }           
                
                


assistant = GenericAssistant('intents.json', intent_methods= mapping)
assistant.train_model()

while True:
    try:
       with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration = 0.5)
            audio = recognizer.listen(mic)
            message = recognizer.recognize_google(audio)
            message = message.lower()
            assistant.request(message)
            
    except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            



