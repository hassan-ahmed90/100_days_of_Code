

THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:

    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window=Tk()
        self.window.title('Quizler')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.score_label=Label(text="Score: 0")
        self.score_label.config(bg=THEME_COLOR,fg='white')
        self.score_label.grid(row=0,column=1)
        self.canvas=Canvas(height=250,width=300)
        self.canvas.config(bg="white")
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.canvas_text=self.canvas.create_text(150,125,width=280,text="This is the question",font=("Arial",20,"italic"),fill=THEME_COLOR)

        right=PhotoImage(file='images/true.png')
        self.buttonright=Button(image=right,highlightthickness=0,command=self.check_ans_right)
        self.buttonright.grid(row=2,column=0)
        wrong = PhotoImage(file='images/false.png')
        self.buttonwrong = Button(image=wrong,highlightthickness=0,command=self.check_ans_wrong)
        self.buttonwrong.grid(row=2, column=1)
        self.next_quiz()


        self.window.mainloop()

    def next_quiz(self):

        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text,text=q_text)
        else:
            self.canvas.config(bg="white")
            self.buttonright.destroy()
            self.buttonwrong.destroy()
            self.canvas.itemconfig(self.canvas_text,text="You have reached to the End of the Game")


    def check_ans_right(self):
        self.give_feedback(self.quiz.check_answer("True")
)
    def check_ans_wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def next_q(self):
        self.canvas.config(bg="white")
        q_text=self.quiz.next_question()
        self.canvas.itemconfig(self.canvas_text,text=q_text)


    def give_feedback(self,right_ans):
        if right_ans:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_quiz)


