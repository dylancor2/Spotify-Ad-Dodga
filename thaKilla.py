import subprocess
import psutil
import keyboard


def close():
    for pid in psutil.pids():
        try:
            if psutil.Process(pid).name() == 'Spotify.exe':
                if psutil.pids().count(pid) > 0:
                    psutil.Process(pid).kill()
                    print("Spotify was killed :D")
        except:
            pass

    
    subprocess.Popen([r"..."]) #put ya location for spotify

keyboard.add_hotkey('ctrl+shift+alt+p', lambda:close()) #Assigns function to script
keyboard.wait('ctrl+shift+alt+p+-') #Ends the script
