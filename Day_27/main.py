import tkinter

window =tkinter.Tk()
window.title("This is my First Program")
window.minsize(width=500,height=300)

my_label =tkinter.Label(text="I'm Label",font=("Arial",24,"bold"))
my_label.pack()
window.mainloop()