#Step 1- Import tikinter
from tkinter import *

#Setp2-  GUI Interaction
window = Tk()

#Step 3- adding inputs
window.geometry('500x500')

checkbox1=IntVar()
checkbox2=IntVar()
checkbox3=IntVar()

chk_btn_1= Checkbutton(window,text='Apple',onvalue=1,offvalue=0,height=2,width=10)
chk_btn_2= Checkbutton(window,text='Mango',onvalue=1,offvalue=0,height=2,width=10)
chk_btn_3= Checkbutton(window,text='Watermelon',onvalue=1,offvalue=0,height=2,width=10)

chk_btn_1.pack()
chk_btn_2.pack()
chk_btn_3.pack()
# Step 4 - Main loop
mainloop()