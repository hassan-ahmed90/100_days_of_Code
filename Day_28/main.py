
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 25
LONG_BREAK_MIN = 20
reps=0
timer=None

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
import math
window=Tk()
window.title("Pomodoro")
window.config(padx=50,pady=50,bg=YELLOW)

def reset_timer():
    window.after_cancel(timer)
    global reps
    reps=0
    canvas.itemconfig(canvas_text,text="00:00")
    timer_label.config(text="Timer",fg=GREEN)
def start_timer():
    global reps
    reps+=1

    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps%8==0:
        timer_label.config(text="Long Break",fg=RED)
        cont_down(long_break_sec)
    elif reps%2==0:
        timer_label.config(text="Short Break",fg=PINK)
        cont_down(short_break_sec)
    else:
        timer_label.config(text="Work",fg=GREEN)

        cont_down(work_sec)

    # if reps<8:
    #     if reps%2==0:
    #         cont_down(work_sec)
    #     elif reps==7:
    #         cont_down(long_break_sec)
    #     else:
    #         cont_down(short_break_sec)





def cont_down(count):
    minute=math.floor(count/60)
    second=count%60
    if second==0:
        second="00"
    elif second<10:
         second=f"0{second}"
    # print(count)
    canvas.itemconfig(canvas_text,text=f"{minute}:{second}")
    if count >0:
        global timer
        timer =window.after(1000,cont_down,count-1)
    else:
        start_timer()
        mark=""
        work_session=math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔"
        pack_label.config(text=mark)


timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,35,"bold"))
timer_label.grid(row=1,column=2)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img=PhotoImage(file="tomato.png")
canvas.create_image(103,112,image=img)
canvas_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)


start_button=Button(text="Start",command=start_timer)
start_button.grid(row=3,column=1)

pack_label=Label(fg=GREEN,bg=YELLOW,pady=10)
pack_label.grid(row=3,column=2)

reset_button=Button(text="Reset",command=reset_timer)
reset_button.grid(row=3,column=3)

window.mainloop()