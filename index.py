#|████████████████████████████████| 3.2 MB 61 kB/s
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 22.6/22.6 MB 7.5 MB/s eta 0:00:00
import sys
import os
from grapheme import startswith
import win32api,win32con
from win10toast import ToastNotifier
toaster = ToastNotifier()
sys.path.append(r'.\lib')
sys.setrecursionlimit(1000000)
import time
import sys
import webbrowser
import datetime
import random
from termcolor import colored  # 导入字体颜色
from colorama import init  # 导入字体颜色
init()  # 初始化字体颜色


import win32com.client as win
from lib import alive_progress_bar
from uefi_boot import UEFI
import inputaz
import open_file_beta


def speak_out(content):
    print(content)
    with open("uefi_boot\\F5.txt", "r") as i:
        Ld = i.read()
    if Ld == "False":
        speak = win.Dispatch("SAPI.SpVoice")
        speak.Speak(content)
def open_app(app_dir):
    os.startfile(app_dir)

from lib import dialogueLib as s
try:
    debug = input("Press Enter to start.Or press ctrl+L to enter the debug-mod.")
    if '\f' in debug:
        UEFI.uefiin()
        print("AI [1.0] remix, for Edexui")
        pass
    else:
        print("AI [1.0] remix, for Edexui")
        time.sleep(1)
        time.sleep(0.5)
        app_dir = r'.\lib\run\run.exe'
        open_app(app_dir)
        alive_progress_bar.apbar()
        os.system("taskkill /f /im run.exe")
        #printImage.printLogo(r".\lib\UEFI5.png")

    #UEFI信息读取
    with open("uefi_boot\\uefi-input-mod.txt", "r") as i:
        INPUT_MOD = i.read()
    print("INPUT_MOD = "+INPUT_MOD)
    with open("uefi_boot\\Install-Game.txt", "r") as i:
        Game_Installed = i.read()
    with open("uefi_boot\\uefi-color-mod.txt", "r") as i:
        TXT_COLOR = i.read()
    print("COLOR_MOD = "+TXT_COLOR)
    
    if TXT_COLOR == "False":
        pass
    else:
        os.system("color "+TXT_COLOR)


    while True:
        if INPUT_MOD == "True":
            pass
        elif INPUT_MOD == "False":
            inputaz.inputa()
            time.sleep(0.02)
        with open("input.txt", "r") as i:
            input_things = i.read()
        a = input_things
        if a in s.baidu:
            webbrowser.open("baidu.com")
            speak_out("jumping to the web site..")

        elif a in s.daohang:
            speak_out("jumping to the web site..")
            webbrowser.open("https://map.baidu.com/")


        elif a in s.fanyi:
            speak_out("coming soon..")
            webbrowser.open("fanyi.baidu.com")

    
        elif a in s.opopo:
            c = input("Please check-on[Y/N]")
            if c == "Y":
                print('OK')
                pi0 = ("shutting down..")
                speak_out(pi0)
                os.system("slidetoshutdown")
            else:
                speak_out("canceled.")

        #beta-debug
        elif (('www.' in a) or ('.html' in a) or ('.htm' in a) or ('.com' in a) or ('.io' in a) or ('.is' in a) or ('.cn' in a) or ('.org' in a)):
            speak_out("jumping..")
            webbrowser.open(a)


        else:
            if a.startswith('run'):  #只有以'run'开头的命令 才执行(因技术所限)
                open_file_beta.openf()
            elif "list app" in a: 
                open_file_beta.list_app()

            elif ('tsk' in a or 'taskkill' in a or 'close' in a):
                open_file_beta.closef()
            
            elif a == "cls":
                os.system("cls")

            else:
                speak_out("Incorrect syntax appears "+"'"+a+"'")



except KeyboardInterrupt:
    print(colored("Warning! You are using 'CTRL + C' to exit!","red"))
    print("exit.")
    time.sleep(2)
