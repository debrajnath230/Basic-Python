#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
window.title('Simple')
window.geometry('400x100')

Label1= Label(window,text='Mail')
Label2= Label(window,text='Password')

e1=Entry(window,width=50,border=5)
e2=Entry(window,width=50,border=5)

Label1.grid(row=0,column=1)
Label2.grid(row=1,column=1)
e1.grid(row=0,column=2)
e2.grid(row=1,column=2)

#Step 4 - main loop
mainloop()