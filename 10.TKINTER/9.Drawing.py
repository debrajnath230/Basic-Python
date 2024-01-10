#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
c = Canvas(window,width=500,height=500)
c.pack()

c.create_line(0,0,500,500,width=5, fill='green',dash=(3,3))
c.create_line(0,500,500,0,width=5, fill='Blue',dash=(3,3))
c.create_rectangle(150,125,450,375,fill='red',outline='Yellow',width=12)

#Step 4 - main loop
mainloop()