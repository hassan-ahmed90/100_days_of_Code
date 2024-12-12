
def add(n1, n2):
    return n1 + n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    if n2!=0:
        return n1/n2

dictionary_cal={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
}

import art
print(art.logo)
while True:
    first_number = int(input("Enter the first number? \n"))
    while True:
        for symbol in dictionary_cal:
            print(symbol)
        operator = input("Enter the operator? \n")

        if operator not in dictionary_cal:
            print("Invalid Operator!")
            continue
        second_number = int(input("Enter the second number? "))
        result=dictionary_cal[operator](first_number,second_number)
        print(f"{first_number} {operator} {second_number} = {result}")
        # if operator =="+":
        #     result=add(first_number,second_number)
        # elif operator =="-":
        #     result=subtract(first_number,second_number)
        # elif operator =="*":
        #     result=multiply(first_number,second_number)
        # elif operator =="/":
        #     result=divide(first_number,second_number)
        # else:
        #     print("Please Enter valid Operator")
        restart=input(f"Type y to continue with {result} or n to restart new calculation? \n type q for exit")
        if restart == "y":
            first_number=result
        elif restart=="n":
            print("\n"*20)
            break
        elif restart=="q":
            print("Good Bye")
            exit()
        else:
            print("Enter valid character")
            exit()









