import webbrowser as wb
import os
import subprocess

class Command_handler:
    """handles the provided command and runs the correct method.
            Commands / KeyWords: shutdown, standby, Steam, open Steam, google, youtube, email
            Just run the script and say the command
        """
    def handler(self, command):
            command = str(command.lower)
            if(command == "shutdown"):
                self.shutdown()
            if(command == "standby"):
                self.standby()
            if(command == "open Steam"):
                self.open_steam()
            else:
                self.open_browser(command)

    def shutdown(self):
        print("shutting down computer")
        os.system("shutdown /s /f /t 200") # forces pc shutdown. Closes all apps automatically.

    def standby(self):
        print("putting computer into standby mode")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0") # put into standby mode. If doesn't work, turn off hibernation feature on machine.

    def open_browser(self, command):
        if(command == "Google"):
            wb.open_new("http://www.google.com")
        if(command == "YouTube"):
            wb.open_new("http://www.youtube.com")
        if(command == 'GMX' or command == 'email'):
            wb.open_new('http://www.gmx.de')
        if (command == 'good horror movie' or command == 'horror movie'):
            wb.open_new('https://www.netflix.com/browse/genre/8711?bc=34399')


    def open_steam(self):
        print("opening steam client")
        subprocess.Popen(["C:\Program Files (x86)\Steam\Steam.exe"])


