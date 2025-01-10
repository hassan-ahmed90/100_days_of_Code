from tkinter import *

windoww=Tk()
windoww.title("Mile to Km Converter")
# windoww.minsize(width=300,height=100)
windoww.config(padx=20,pady=20)


my_intry=Entry(width=8)
my_intry.grid(column=1,row=0)

label1=Label(text="Miles")
label1.grid(column=2,row=0)


label2=Label(text="is equal to:")
label2.grid(column=0,row=3)


label3=Label(text="0")
label3.grid(column=1,row=3)

label4=Label(text="Km")
label4.grid(column=2,row=3)

def my_button():
    miles=my_intry.get()
    km=int(miles)*1.60934
    label3.config(text=km)

button=Button(text="Calculate",command=my_button)
button.grid(row=4,column=1)
windoww.mainloop()