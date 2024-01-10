#Step 1- Import tikinter
from tkinter import *
import tkinter.messagebox
#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
tkinter.messagebox.showinfo('Info','Hello World')
question= tkinter.messagebox.askokcancel('Weather','Will it rain')

if question == True:
    print('Take an umbrella')
    
else:
    print('Ok')    

#Step 4 - main loop
mainloop()