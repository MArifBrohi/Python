# Python program to convert
# text to speech

# import the required module from text to speech conversion
import win32com.client

# Calling the Dispatch method of the module which
# interact with Microsoft Speech SDK to speak
# the given input from the keyboard

speaker = win32com.client.Dispatch("SAPI.SpVoice")


print("Enter the word you want to speak it out by computer")
s = input()
speaker.Rate = 1.0

speaker.Volume = 100
speaker.speak(s)


# To stop the program press
# CTRL + Z
