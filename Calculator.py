import imp
from tkinter import *
root = Tk()
root.title('CuiMoo\'s Calculator 0.1')


content = ''
text_input = StringVar(value='0')

def btn(number):
    global content
    content = content + str(number)
    text_input.set(content)

def equal():
    global content
    calculate = float(eval(content))
    text_input.set(calculate)
    content = ''

def clear():
    global content
    content = ''
    text_input.set('')
    display.insert(0,'0')


#Display 5x4
display = Entry(font=('arial',30,'bold'),fg='black',bg='#caeceb',textvariable=text_input,justify='right')
display.grid(columnspan=4)


# Input via Button

#row1
btn7 = Button(text='7',font = ('arial',30,'bold'),command=lambda:btn(7),padx=30,pady=15).grid(row=1,column=0)
btn8 = Button(text='8',font = ('arial',30,'bold'),command=lambda:btn(8),padx=30,pady=15).grid(row=1,column=1)
btn9 = Button(text='9',font = ('arial',30,'bold'),command=lambda:btn(9),padx=30,pady=15).grid(row=1,column=2)
btnc = Button(text='c',font = ('arial',30,'bold'),command=clear,padx=30,pady=17,bg='#00ffbf').grid(row=1,column=3)

#row2
btn4 = Button(text='4',font = ('arial',30,'bold'),command=lambda:btn(4),padx=30,pady=15).grid(row=2,column=0)
btn5 = Button(text='5',font = ('arial',30,'bold'),command=lambda:btn(5),padx=30,pady=15).grid(row=2,column=1)
btn6 = Button(text='6',font = ('arial',30,'bold'),command=lambda:btn(6),padx=30,pady=15).grid(row=2,column=2)
btn_P = Button(text='+',font = ('arial',30,'bold'),command=lambda:btn('+'),padx=30,pady=15,bg='#00ffbf').grid(row=2,column=3)

#row3
btn1 = Button(text='1',font = ('arial',30,'bold'),command=lambda:btn(1),padx=30,pady=15).grid(row=3,column=0)
btn2 = Button(text='2',font = ('arial',30,'bold'),command=lambda:btn(2),padx=30,pady=15).grid(row=3,column=1)
btn3 = Button(text='3',font = ('arial',30,'bold'),command=lambda:btn(3),padx=30,pady=15).grid(row=3,column=2)
btn_M = Button(text='-',font = ('arial',30,'bold'),command=lambda:btn('-'),padx=35,pady=15,bg='#00ffbf').grid(row=3,column=3)

#row4
btn0 = Button(text='0',font = ('arial',30,'bold'),command=lambda:btn(0),padx=30,pady=15).grid(row=4,column=1)
btn_Dot = Button(text='.',font = ('arial',30,'bold'),command=lambda:btn('.'),padx=36,pady=15).grid(row=4,column=0)
btn_Di = Button(text='÷',font = ('arial',30,'bold'),command=lambda:btn('/'),padx=30,pady=15,bg='#00ffbf').grid(row=4,column=2)
btn_Mul = Button(text='x',font = ('arial',30,'bold'),command=lambda:btn('*'),padx=30,pady=15,bg='#00ffbf').grid(row=4,column=3)

#row5
btn_Eq = Button(text='=',font = ('arial',30,'bold'),command=equal,padx=90,pady=15,bg='#0080ff').grid(row=5,column=2,columnspan=2)
btn_Open = Button(text='(',font = ('arial',30,'bold'),command=lambda:btn('('),padx=36,pady=15).grid(row=5,column=0)
btn_Close = Button(text=')',font = ('arial',30,'bold'),command=lambda:btn(')'),padx=36,pady=15).grid(row=5,column=1)



root.mainloop()
