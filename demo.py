import speech_recognition as sr
import webbrowser as wb

r2 = sr.Recognizer()
r3 = sr.Recognizer()

with sr.Microphone() as source:
        print("speak now")
        audio = r3.listen(source)

with open(r"key.json", "r") as f:
    credentials_json = f.read()

if "Google" in r2.recognize_google_cloud(audio, credentials_json=credentials_json):
    print("detected Google")
    wb.get().open_new("https://www.google.com/")

if "youtube" in r2.recognize_google_cloud(audio, credentials_json=credentials_json):
    print("detected youtube")
    wb.get().open_new("https://www.youtube.com/")