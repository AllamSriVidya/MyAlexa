
import speech_recognition as sr
import pywhatkit
import pyttsx3
import wikipedia
import datetime
import pyjokes
import pyaudio

listener=sr.Recognizer()
engine=pyttsx3.init()



def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        engine.setProperty('voice','com.apple.speech.synthesis.voice.zuzana')
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration = 1)
            print('listening......') 
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            if 'alexa' in command:
                command=command.replace('alexa','')
                print(command)
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e)) 
          
    except sr.UnknownValueError: 
        print("unknown error occured") 
    
    except LookupError:                          
        print("Could not understand audio")
       
    return command

def run_alexa(): 
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play',' ')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now()
        talk(time)
        print(time)
    elif 'who is' in command:
        person=command.replace('who is','')
        info= wikipedia.summary(person,1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_jokes)
    elif 'date' in command:
        talk('sorry iam busy')
    else:
        talk('I dont understand what you are saying')

while(1):
        run_alexa()
   