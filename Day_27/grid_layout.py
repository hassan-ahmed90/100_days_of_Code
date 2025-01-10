from tkinter import *


window =Tk()
window.title("This is my First Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

my_label =Label(text="New Label",font=("Arial",20,"bold"))
my_label.grid(column=0,row=0)


my_button=Button(text="Click Me")
my_button.grid(row=1,column=1)

new_intry=Entry()
new_intry.grid(row=2,column=3)

custom_button=Button(text="New Button")
custom_button.grid(row=0,column=2)
window.mainloop()