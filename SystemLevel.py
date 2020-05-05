import webbrowser as wb
import os


def function(string):
    if(string == "shutdown"):
        print("shutting down computer")
        os.system("shutdown /s /f /t 3") # forces pc shutdown. Closes all apps automatically.
