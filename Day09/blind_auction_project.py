

def find_highest_bid(bidding_dictionary):
    winner = ""
    highest_bid = 0
    for bidder in bidding_dictionary:
        bidder_amount = bidding_dictionary[bidder]
        if bidder_amount > highest_bid:
            highest_bid = bidder_amount
            winner = bidder

    print(f" The winner is {winner} with the bid of {highest_bid}")
import art
print(art.logo)
dictionary_bid={}
while True:
    name=input("Enter your name? \n")
    bid=int(input("What is your bid? $\n"))

    dictionary_bid[name]=bid

    restart=input("Are there any bidders 'yes' or 'no' ")
    if restart!="yes":
        find_highest_bid(dictionary_bid)

        # highest = max(dictionary_bid, key=dictionary_bid.get)
        # print(f"The winner is {highest} with the bid of {dictionary_bid[highest]}")
        break



