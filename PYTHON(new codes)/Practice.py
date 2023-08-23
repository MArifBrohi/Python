import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

print('''Welcome to the RoboSpeaker!
What you want me to speak?''')
s = input()
speaker.Speak(s)