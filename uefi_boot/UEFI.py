from uefi_boot import loadlib_uefi
import os
import sys
import time
from termcolor import colored  # 导入字体颜色
from colorama import init  # 导入字体颜色
init()  # 初始化字体颜色

def uefiin():
    loadlib_uefi.load
    print("To Enter UEFI boot,press Ctrl+L and Enter.")
    print("Or,press Enter")
    char = input(">")
    if '\f' in char:
        print("preparing uefi...")
        loadlib_uefi.load()
        time.sleep(2)
        print("")
        try:
            while True:
                #==================================================
                with open("uefi_boot\\uefi-input-mod.txt", "r") as i:
                    TXT_INPUT = i.read()
                INPUT_MOD = TXT_INPUT
                with open("uefi_boot\\uefi-color-mod.txt", "r") as ii:
                    TXT_COLOR = ii.read()
                COLOR_MOD = TXT_COLOR
                #==================================================
                print(colored("Please check the help file carefully before doing this step! Otherwise, the system may crash! (REALLY!)","red"))
                print("""
            PRESS CTRL+C TO SAVE AND EXIT!
            PRESS CTRL+L TO RESTORE ALL SETTINGS!

            A.CHANGE INPUT MOD
            B.CHANGE COLOR
            C.F5 MOD
                """)
                uu = input("")
                if uu == "A":
                    print("[TXT-INPUT]  " + INPUT_MOD)
                    asc = input("[T/F/P] ")
                    if asc == "T":
                        tt = ("True")
                        for i in range(2):
                            file = open('uefi_boot\\uefi-input-mod.txt', 'w+')
                            file.write(tt)
                            time.sleep(2)
                    elif asc == "P":
                        print("PASS!")
                        time.sleep(2)
                    else:
                        ff = ("False")
                        for i in range(2):
                            file = open('uefi_boot\\uefi-input-mod.txt', 'w+')
                            file.write(ff)
                            time.sleep(2)

                elif uu == "B":
                    print("[OUTPUT-COLOR]  " + COLOR_MOD)
                    asc = input("[PRESS YOUR COLOR (NEED HELPS? PRESS 'H')] ")
                    if uu == "H":
                        print("请查看 ./uefi_boot/uefi_help.md")
                    else:
                        for i in range(2):
                            file = open('uefi_boot\\uefi-color-mod', 'w+')
                            file.write(tt)
                            time.sleep(2)



                elif '\f' in uu:
                    lll = "False"
                    ppp = "True"
                    for i in range(5):
                        #==========================================
                        file = open('uefi_boot\\uefi-input-mod.txt', 'w+')
                        file.write(lll)

                        file = open('uefi_boot\\uefi-color-mod.txt', 'w+')
                        file.write(lll)
                        time.sleep(2)
                        # ==========================================

                os.system("cls")


        except KeyboardInterrupt:
            print(colored("save and exit uefi boot! (ctrl+c)", "red"))
            time.sleep(5)
            os.system("cls")