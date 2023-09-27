from tkinter import *
from Tempsensor import *
import time
import threading
import lcdlib
import RPi.GPIO as GPIO

root = Tk()
root.title('Temperature Monitoring')
root.geometry('500x500+50+50')


oTempsensor = Sensor()
temp,humid  =oTempsensor.get_temp_humid()

lcd = lcdlib.lcd()

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
relay1 = 17
relay2 = 27
GPIO.setup(relay1, GPIO.OUT)
GPIO.setup(relay2, GPIO.OUT)
GPIO.output(relay1,True)
GPIO.output(relay2,True)


FONT1 = (None,40)
FONT2 = (None,40,'bold')

L1 = Label(root,text='Temperature',font = FONT1)
L1.pack(pady=20)
# Temperature display

v_temp = StringVar()
v_humid = StringVar()

v_temp.set(f'{temp} c')
v_humid.set(f'{humid}%')

def UpdateTemp():
    global temp,humid
    temp , humid =oTempsensor.get_temp_humid()
    v_temp.set(f'{temp:.1f}°c')
    lcd.lcd_clear()
    lcd.lcd_display_string(f'  TEMP: {temp:.1f} c',1)
    lcd.lcd_display_string(f'  HUMID: {humid:.1f}%',2)
    

def RunUpdateTemp():
    while True:
        try:
            UpdateTemp()
            
            if float(temp) >=29.5:
                GPIO.output(relay2,False)
            else:
                GPIO.output(relay2,True)

        except:
            v_temp.set('ERROR')
            lcd.lcd_clear()
            lcd.lcd_display_string(f'ERROR',1)
            
        time.sleep(5)

    
L2 =Label(root,textvariable =v_temp ,font=FONT2 ,fg='blue')
L2.pack(pady=20)

L3 = Label(root,text='Humidity',font = FONT1)
L3.pack(pady=20)

L4 =Label(root,textvariable =v_humid ,font=FONT2 ,fg='blue')
L4.pack(pady=20)

B = Button(root,text='Update',command=UpdateTemp)
B.pack()


task = threading.Thread(target=RunUpdateTemp)
task.start()

root.mainloop()


