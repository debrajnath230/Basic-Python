#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
window.title('Simple')
window.geometry('500x700')
window.config(bg='Green')
frame1=Frame(window, width= 300, height=200,cursor='dot')
frame2=Frame(window, width= 300, height=200,cursor='dotbox')

button1=Button(frame1,text='Button1', bg='Blue')
button2=Button(frame2,text='Button2', bg='Pink')
button3=Button(frame1,text='check', bg='Pink')
frame1.pack(side=TOP)
frame2.pack(side=BOTTOM)
button1.pack()
button2.pack()
button3.pack()
#Step 4 - main loop
mainloop()
