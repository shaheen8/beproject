import os
from methods import playVideo as pl
shpfiles = []
import cv2


path = "C:\\Users\\shaheen\\Desktop\\input-videos\\"
vidpath = ''
fullpath=''
def signRecog(self,text):
    print("text is :", text)

    for dirpath, subdirs, files in os.walk(path):
        for x in files:
            txt = text.split(" ")
            t = txt[0]
            print("strts wid ::", t)
            if x.startswith(t):
                vidpath = x
                fullpath = os.path.join(path + x)
                break
    print("We get video name ::", vidpath)
    print("We get video path ::", fullpath)
    pl.play(self, fullpath)
