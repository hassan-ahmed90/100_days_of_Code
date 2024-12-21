from quiz_brain import QuizBrain
from data import question_data
from question_model import Question

question_bank=[]

for item in question_data:
    ques=item['question']
    ans=item['correct_answer']
    quiz=Question(ques,ans)
    question_bank.append(quiz)


quiz1=QuizBrain(question_bank)
quiz1.next_question()

while quiz1.still_has_question():
    quiz1.next_question()

print("You have completed the quiz !")
print(f"Your final Score is {quiz1.score}")