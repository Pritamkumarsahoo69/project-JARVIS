from Brain.AIBrain import ReplyBrain
from Brain.Qna import QuestionsAnswer
from Body.Listen import MicExecution
print(">> Starting The Jarvis : Wait For Some Seconds <<")
from Body.speak import Speak
from Features.clap import Tester
print(">> Starting The Jarvis : Wait For Few Seconds More <<")
#from main import MainTaskExecution
from text import MainTaskExecution
def MainExecution():

    Speak("Hello sir!,I'm Jarvis")
    Speak("we are online and ready")

    while True:
        Data = MicExecution()
        Data = str(Data)

        ValueReturn = MainTaskExecution(Data)
        if ValueReturn==True:
            pass
        elif len(Data)<3:
            pass
        elif "what is" in Data or "where is" in Data or "answer" in Data:
            reply = QuestionsAnswer(Data)
        else:
            reply = ReplyBrain(Data)
            Speak(reply)
        
def ClapDetected():
    query = Tester()
    if "True-mic" in query:
        print("")
        print(">> clap Detected! <<")
        print("")
        MainExecution()
    else:
        pass
ClapDetected()
MainExecution()