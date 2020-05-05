import webbrowser as wb
import os


def shutdown(string):
    if(string == "shutdown"):
        print("shutting down computer")
        os.system("shutdown /s /f /t 3") # forces pc shutdown. Closes all apps automatically.

def standby(string):
    if(string == "shutdown"):
        print("putting computer into standby mode")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") # put into standby mode. If doesn't work, turn off hibernation feature on machine.

def open_browser(command):
    wb.open_new("http://www.google.com")