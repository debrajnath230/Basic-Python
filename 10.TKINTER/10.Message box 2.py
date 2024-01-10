# Step 1 - Import tkinter
from tkinter import *

# Step 2 - GUI Interaction
window = Tk()

# Step 3 - Adding inputs
# window.geometry('400x100')
# var = StringVar()  # Add parentheses here
# Message = Message(window, textvariable=var, relief=RAISED,padx=20,pady=20)
# var.set('Welcome')
# Message.pack()

var=StringVar()
ent_var=StringVar()
def insert():
    result=ent_var.get()
    var.set(result)
    
message=Message(window,textvariable=var,relief=RAISED,padx=50,pady=50)
entry=Entry(window,textvariable=ent_var)
button=Button(window,text="Ok",command=insert)
message.pack()
entry.pack()
button.pack()

# Step 4 - Main loop
mainloop()
