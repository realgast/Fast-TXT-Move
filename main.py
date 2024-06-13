import os
import time
import colorama
from colorama import Fore, Back, Style
import shutil

colorama.init()

def zczytywanieappdaty():
    return os.path.join(os.environ['USERPROFILE'], 'AppData', 'Roaming', '.minecraft', 'resourcepacks')

def move_file(file_path, new_location):
    if not os.path.exists(new_location):
        os.makedirs(new_location)
    shutil.move(file_path, new_location)
    print(Fore.MAGENTA + "[F] " + Fore.WHITE + "I got you ;)")

def mainscreen():
    local_appdata_path = zczytywanieappdaty()
    print(Fore.MAGENTA + "[F] " + Fore.WHITE + "Welcome to Fast TXT Move ")
    print(Fore.MAGENTA + "[F] " + Fore.WHITE + "Drop your texturepack file here: ")
    print(Fore.MAGENTA + "[F] " + Fore.WHITE + "When you drop your texturepack press enter to continue")
    file_path = input().strip('"')
    if not os.path.isfile(file_path):
        print("Wrong file path, try again.")
        return
    move_file(file_path, local_appdata_path)
    time.sleep(3)

mainscreen()
