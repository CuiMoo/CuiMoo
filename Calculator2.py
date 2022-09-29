from tkinter import *
from tkinter import ttk , messagebox


window = Tk()
window.title('CuiMoo\'s Calculator 1.0')

content = ''
text_in = StringVar(value='0')
btn1bg='#dbe3ab'
btn2bg='#e3b3ab'
def pb(number):
    global content
    content = content+str(number)
    text_in.set(content)

def equal():
    global content
    cal = float(eval(content))
    text_in.set(cal)
    print(text_in.get(),type(text_in.get()))
    content=''

def clear():
    global content
    content = ''
    text_in.set('')
    display.insert(0,'0')

def dell():
    global content
    dat=str(text_in.get())
    content=dat[:-1]
    text_in.set(content)
#Display
display = Entry(font=('Franklin Gothic',30),fg='black',bg='#caeceb',textvariable=text_in,justify='right')
display.grid(columnspan=4)

#row1
btn7 = Button(text='7',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(7)
                                                    ).grid(row=1,column=0)
btn8 = Button(text='8',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(8)
                                                    ).grid(row=1,column=1)
btn9 = Button(text='9',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(9)
                                                    ).grid(row=1,column=2)
btnP = Button(text='+',font=('arial',30,'bold'),bg=btn2bg,padx=28,pady=15,command=lambda:pb('+')
                                                    ).grid(row=1,column=3)

#row2
btn4 = Button(text='4',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(4)
                                                    ).grid(row=2,column=0)
btn5 = Button(text='5',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(5)
                                                    ).grid(row=2,column=1)
btn6 = Button(text='6',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(6)
                                                    ).grid(row=2,column=2)
btnMi = Button(text='-',font=('arial',30,'bold'),bg=btn2bg,padx=33,pady=15,command=lambda:pb('-')
                                                    ).grid(row=2,column=3)

#row3
btn1 = Button(text='1',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(1)
                                                    ).grid(row=3,column=0)
btn2 = Button(text='2',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(2)
                                                    ).grid(row=3,column=1)
btn3 = Button(text='3',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(3)
                                                    ).grid(row=3,column=2)
btnMu = Button(text='x',font=('arial',30,'bold'),bg=btn2bg,padx=29,pady=15,command=lambda:pb('*')
                                                    ).grid(row=3,column=3)

#row4
btnDot = Button(text='·',font=('arial',30,'bold'),bg=btn1bg,padx=32,pady=15,command=lambda:pb('.')
                                                    ).grid(row=4,column=0)
btn0 = Button(text='0',font=('arial',30,'bold'),bg=btn1bg,padx=27,pady=15,command=lambda:pb(0)
                                                    ).grid(row=4,column=1)
btnC = Button(text='C',font=('arial',30,'bold'),padx=24,pady=15,bg='#eda64a',command=clear
                                                    ).grid(row=4,column=2)
btnDi = Button(text='÷',font=('arial',30,'bold'),bg=btn2bg,padx=28,pady=15,command=lambda:pb('/')
                                                    ).grid(row=4,column=3)

#row5
btnOpen = Button(text='(',font=('arial',30,'bold'),padx=32,pady=15,command=lambda:pb('(')
                                                    ).grid(row=5,column=0)
btnClose = Button(text=')',font=('arial',30,'bold'),padx=32,pady=15,command=lambda:pb(')')
                                                    ).grid(row=5,column=1)
btnDel = Button(text='del',font=('arial',30,'bold'),bg='#d86769',padx=10,pady=15,command=dell
                                                    ).grid(row=5,column=2)
btnEqu = Button(text='=',font=('arial',30,'bold'),bg='#cfabe3',padx=28,pady=15,command=equal
                                                    ).grid(row=5,column=3)


window.mainloop()
