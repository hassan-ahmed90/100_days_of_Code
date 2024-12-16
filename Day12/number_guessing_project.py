import random

import art
print(art.logo)
print("Welcome to Number Gussing Game")
print("I'm Thinking of a number between 1 to 100")
difficulty_level=input("Choose difficulty level type 'easy' or 'hard'\n ")
choosed_number=random.randint(0,100)


def win_check(attemptss):
    while attemptss>0:
        print(f"You have {attemptss} attempts remaining to guess the number")
        guess_number=int(input("Make a guess\n"))
        if guess_number==choosed_number:
            print("You Win")
            break
        elif guess_number>choosed_number:
            print("too high")
            attemptss-=1
        elif guess_number<choosed_number:
            print("too low")
            attemptss-=1

        if attemptss==0:
            print("You are run out of guess you loose")
            print(f"The number was {choosed_number}")

if difficulty_level=='easy':
    win_check(10)
elif difficulty_level=='hard':
    win_check(5)
else:
    print("Enter valid choice")

