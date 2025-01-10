from tkinter import *

window =Tk()
window.title("This is my First Program")
window.minsize(width=500,height=300)

my_label =Label(text="I'm Label",font=("Arial",24,"bold"))
my_label.pack()
my_label['text']="New Text"
my_label.config(text="Your Text")

def button_clicked():
    my_label.config(text=intry.get())

my_button=Button(text="Click Me",command=button_clicked)
my_button.pack()

intry=Entry()
intry.insert(END,string="Text to begin")
intry.pack()
print(intry.get())

text=Text(height=5,width=30)
text.focus()
text.insert(END,"Example of multi line Entry")
print(text.get("1.0",END))
text.pack()

def spin_used():
    print(spinbox.get())
spinbox=Spinbox(width=5,from_=0,to=10,command=spin_used)
spinbox.pack()

def check_used():
    print(check_state.get())
check_state=IntVar()
checkbox=Checkbutton(text="is On?",variable=check_state,command=check_used)
checkbox.pack()

def scale_used(value):
    print(value)
scale=Scale(from_=0,to=90,command=scale_used)
scale.pack()

def radio_used():
    print(radio_state.get())
radio_state=IntVar()
radioButton=Radiobutton(text="Option1",value=1,variable=radio_state,command=radio_used)
radioButton2=Radiobutton(text="Option2",variable=radio_state,value=2,command=radio_used)
radioButton.pack()
radioButton2.pack()

def listbox_used(event):
    print(list_box.get(list_box.curselection()))
list_box=Listbox(height=4)
fruits=["Apple","Banana","Stawberry","Mango","Orange"]
for item in fruits:
    list_box.insert(fruits.index(item),item)

list_box.bind("<<ListboxSelect>>",listbox_used)
list_box.pack()

window.mainloop()
