# healthy pf
import time

from pygame import mixer
from datetime import datetime
from time import time
def musicloop(file1,stopper):
    mixer.init()
    mixer.music.load('file1.mp3')
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log(msg):
    with open("normal.txt","a") as f:
        f.write(f"{msg}{datetime.now()}\n")
if __name__ == '__main__':

    init_water=time()
    init_eyes=time()
    init_exe=time()
    water=10
    eyes=15
    exe=25
    while True:
        if time()-init_water > water:
            print("Time to drink water , press stop to stop the music")
            musicloop("file1.mp3","stop")
            init_water= time()
            log("Drank water at")


        if time()-init_eyes>eyes:
            print("Time to close eyes , press stop to stop the music")
            musicloop("file1.mp3","stop")
            init_eyes = time()

            log("Eyes closed at ")

        if time()-init_exe>exe:
            print("Time for exercise , press stop to stop the music")

            musicloop("file1.mp3","stop")
            init_exe = time()

            log("Exececised at ")





