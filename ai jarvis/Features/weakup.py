import speech_recognition as sr
import os

def Listen():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,0,5) 

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="en")
    except:
        return ""
    
    query = str(query).lower()
    print(query)
    return query

def WakeupDetected():
    queery = Listen().lower()
        
    if "wake up Jarvis" in queery:
        os.startfile(r"F:\\ai jarvis\\jarvis2.0.py")
        
    else:
        pass