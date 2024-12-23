import os
import keyboard
import pyautogui
import webbrowser
from time import sleep
def OpenExe(Queary):
    Queary = str(Queary).lower()

    if "visit" in Queary:
        Nameofweb = Queary.replace("visit","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "launch" in Queary:
        Nameofweb = Queary.replace("launch","")
        Link = f"https://www.{Nameofweb}.com"
        webbrowser.open(Link)
        return True

    elif "open" in Queary:
        Nameoftheapp = Queary.replace("open","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True
    
    elif "start" in Queary:
        Nameoftheapp = Queary.replace("start","")
        pyautogui.press('win')
        sleep(1)
        keyboard.write(Nameoftheapp)
        sleep(1)
        keyboard.press('enter')
        sleep(0.5)
        return True