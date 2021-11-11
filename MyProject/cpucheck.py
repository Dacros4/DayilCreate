#Hey this script is for linux!

import tkinter,time
from tkinter import *
import tkinter.messagebox

warntemp = 49 #change it :V

top = Tk()
top.withdraw()
while 1:
    f = open('/sys/class/thermal/thermal_zone0/temp','r')
    ts = f.read()
    t = int(ts) / 1000
    print("CPU Temp:"+str(t)+"oC")
    if t >= warntemp:
        tkinter.messagebox.showerror("CPU Temp Check",'CPU Temp is too high!Temp:'+str(t)+"oC")
    time.sleep(6)
