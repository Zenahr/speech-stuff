import webbrowser as wb
import os
import subprocess


def shutdown(command):
    if(command == "shutdown"):
        print("shutting down computer")
        os.system("shutdown /s /f /t 200") # forces pc shutdown. Closes all apps automatically.

def standby(command):
    if(command == "shutdown"):
        print("putting computer into standby mode")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") # put into standby mode. If doesn't work, turn off hibernation feature on machine.

def open_browser(command):
    wb.open_new("http://www.google.com")

def open_steam(command):
        if(command == "shutdown"):
            print("opening steam client")
            subprocess.Popen(["C:\Program Files (x86)\Steam\Steam.exe"])