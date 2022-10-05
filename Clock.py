from os import access
from tkinter import *
from datetime import datetime
import time

clock = Tk()
clock.title('CuiMoo\'s CLOCK')
fnt = 'Agency FB'

def time():
    now =datetime.now()
    stime = now.strftime('%H:%M:%S')
    day = now.strftime('Week:%W \nDate %d %B %Y')
    lbl1.config(text=stime)
    lbl2.config(text=day)
    lbl1,lbl2.after(1000,time)
    

lbl1 = Label(clock,font=(fnt,30,'bold'),bg='light green',fg='black')
lbl1.pack(anchor='center')
lbl2 = Label(clock,font=(fnt,30,'bold'),fg='red')
lbl2.pack(anchor='center')
time()


clock.mainloop()
