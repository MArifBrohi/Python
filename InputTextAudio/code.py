# if you run this program, firstly it generates errors

           # to resolve those error follow following steps

           # 1: pip install pyttsx3
                    # maybe this will generate an error during the middle of installation so what...
           # 2: pip install pypiwin32


    # Code will run without any penny of difficulty

import pyttsx3
s = input("Enter any text: ")
engine = pyttsx3.init()
engine.say(s)
engine.runAndWait()
