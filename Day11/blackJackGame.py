import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card

def sumCard(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(u_score,c_score):
    if u_score==c_score:
        print("Draw")
    elif c_score==0:
        print("You Lose")
    elif u_score==0:
        print("You Win")
    elif c_score>21:
        print("You win")
    elif u_score>21:
        print("You Lose")
    elif c_score<u_score:
        print("You Win")
    else:
        print("You Lose")

def play():
    # print(art.logo)
    user_card=[]
    comp_card=[]
    user_score=-1
    comp_score=-1
    is_game_play=False

    for _ in range(2):
        user_card.append(deal_card())
        comp_card.append(deal_card())
    while not is_game_play:
        user_score=sumCard(user_card)
        comp_score=sumCard(comp_card)
        print(f"The User cards {user_card} and score is {user_score}")
        print(f"The Computer first card {comp_card[0]}")

        if user_score==0 or comp_score==0 and user_score>21:
            is_game_play=True
        else:
            user_deal=input("Type y to get card or n to pass? \n")
            if user_deal=='y':
                user_card.append(deal_card())
            else:
                is_game_play=True
    while comp_score!=0 and comp_score<17:
        comp_card.append(deal_card())
        comp_score=sumCard(comp_card)
    print(f"User cards {user_card} and score {user_score}")
    print(f"Computer cards {comp_card} and score {comp_score}")
    print(compare_score(user_score,comp_score))

while input("Do you want to play BlackJack game Type y to play and n to not? \n")=='y':
    print("\n"*20)
    play()
