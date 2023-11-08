import time, os, keyboard
from pygame import mixer


mixer.init()
os.system('cls')




mixer.music.load("Mini Boss.mp3")

time="00:00"
wast=""
def pad(num):
    out = ""
    if num<10:
        out = "0"
    out += str(num)
        
    return out


while True:
    mixer.music.play()
    t=0
    while mixer.music.get_busy():
        if not t==wast:
            os.system('cls')
            print(time)

        wast=t
        t=mixer.music.get_pos()
        t//=1000
        m = t//60
        s = t%60
        time=pad(m)+":"+pad(s)
