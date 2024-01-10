#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs

menu =Menu(window)
file =Menu(menu,tearoff=0)
file.add_command(label='New')
file.add_command(label='open')
file.add_command(label='Save')
file.add_command(label='Print')
file.add_separator()
file.add_command(label='exit',command=window.quit)

menu.add_cascade(label='File',menu=file)
window.config(menu=menu)

#Step 4 - main loop
mainloop()