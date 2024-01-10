#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
window.geometry('500x500')

button=Button(window,text='Button',width=12,bg='Red',fg='White')
button.place(x=200,y=100)

# Step 4 - Main loop
mainloop()