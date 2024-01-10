#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
window.title('Simple')
window.geometry('400x100')

def log_entry():
    print('Logged in')

button1=Button(window,text='Log in',command=log_entry,width=12, bg='red',fg='white',font=('Bold',12),activebackground='black',activeforeground='white')
button1.pack()

#Step 4 - main loop
mainloop()