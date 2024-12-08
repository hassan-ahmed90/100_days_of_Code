rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def myfuction():
    print("Your Choice")
    if userChoice==0:
        print("Rock")
        print(rock)
    elif userChoice==1:
        print("Paper")
        print(paper)
    else:
        print("Scissors")
        print(scissors)
    print("Computer Choice")
    if comuterChoice==0:
        print("Rock")
        print(rock)
    elif comuterChoice==1:
        print("Paper")
        print(paper)
    else:
        print("Scissors")
        print(scissors)
import random
userChoice=int(input("What do you choose\nType 0 for Rock\nType 1 for Paper\n2 for Scissors\n"))
comuterChoice= random.randint(0,2)
if userChoice==comuterChoice:
    myfuction()
    print("Game Tie")
elif comuterChoice==0 and userChoice==1:
    myfuction()
    print("You Win")
elif comuterChoice==1 and userChoice==0:
    myfuction()
    print("You Loose")
elif comuterChoice==2 and userChoice==1:
    myfuction()
    print("You Loose")
elif comuterChoice==1 and userChoice==2:
    myfuction()
    print("You Win")
elif comuterChoice==2 and userChoice==0:
    myfuction()
    print("You Win")
elif comuterChoice==0 and userChoice==2:
    myfuction()
    print("You Loose")






