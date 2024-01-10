#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
window.title('Simple')
window.geometry('400x100')

label1=Label(window,text='Label-1',bg='red',fg= 'white')
label2=Label(window,text='Label-2',bg='Blue',fg= 'white')
label3=Label(window,text='Label-3',bg='violet',fg= 'white')

label1.pack(side=TOP,fill=X,expand=FALSE)
label2.pack(side=LEFT,fill=Y,expand=FALSE)
label3.pack(side=RIGHT,fill=Y,expand=FALSE)
#Step 4 - main loop
mainloop()