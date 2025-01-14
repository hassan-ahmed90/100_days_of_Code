from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.title('FlashCard App')
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR,highlightthickness=0)

current_card={}

def remove_card():
    global my_dict
    if current_card in my_dict:
        my_dict.remove(current_card)
        pd.DataFrame(my_dict).to_csv('data/remaining_words.csv',index=False)
        next_card()


def next_card():
    if my_dict:
        global current_card,flip_timer
        window.after_cancel(flip_timer)
        current_card = random.choice(my_dict)
        canvas.itemconfig(vocab_text,text=current_card["French"],fill="black")
        canvas.itemconfig(title_text,text="French",fill="black")
        canvas.itemconfig(canvas_image,image=photo_front)
        flip_timer=window.after(3000, func=flip_card)
    else:
        canvas.itemconfig(vocab_text, text="You've learned all words!", fill="black")
        canvas.itemconfig(title_text, text="Congratulations!", fill="black")
        canvas.itemconfig(canvas_image, image=photo_front)
        button_right.config(state="disabled")
        button_wrong.config(state="disabled")


def flip_card():
    canvas.itemconfig(canvas_image,image=photo_back)
    canvas.itemconfig(title_text,text="English",fill="white")
    canvas.itemconfig(vocab_text,text=current_card["English"],fill="white")



photo_front=PhotoImage(file='images/card_front.png')
photo_back=PhotoImage(file='images/card_back.png')
canvas=Canvas(width=800,height=526,highlightthickness=0)
canvas_image=canvas.create_image(400,262,image=photo_front)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)
title_text=canvas.create_text(400,150,text="French",fill="black",font=("Ariel",40,"italic"))
vocab_text=canvas.create_text(400,263,text="trouve",fill="black",font=("Ariel",60,"bold"))

right_image=PhotoImage(file='images/right.png')
wrong_image=PhotoImage(file='images/wrong.png')


button_right=Button(image=right_image, highlightthickness=0, command=remove_card)
button_right.grid(row=1,column=1)


button_wrong=Button(image=wrong_image, highlightthickness=0, command=next_card)
button_wrong.grid(row=1,column=0)


import pandas as pd
import random

try:
    df=pd.read_csv('data/remaining_words.csv')
    my_dict=df.to_dict(orient="records")
except FileNotFoundError:
    df = pd.read_csv('data/french_words.csv')
    my_dict=df.to_dict(orient="records")

flip_timer=window.after(3000,func=flip_card)
next_card()


window.mainloop()