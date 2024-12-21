
class QuizBrain:
    def __init__(self,question_list):
        self.score=0
        self.question_no=0
        self.question_list=question_list

    def still_has_question(self):
        if self.question_no<len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_ans,correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You guess Right !")
            print(f"Your score {self.question_no}/{self.score}")
        else:
            print("You guess Wrong")
            print(f"Your score {self.question_no}/{self.score}")



    def next_question(self):
        current_question=self.question_list[self.question_no]
        self.question_no+=1
        user_guess=input(f"Q {self.question_no}: {current_question.question} T/F ?")
        self.check_answer(user_guess,current_question.answer)








