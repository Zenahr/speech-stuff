import speech_recognition as sr
import Commands as co

r2 = sr.Recognizer()
r3 = sr.Recognizer()
handler = co.Command_handler()

with sr.Microphone() as source:
        print("speak now")
        audio = r3.listen(source)


recognized_audio = r2.recognize_google(audio)
handler.handler(recognized_audio)
print(recognized_audio)