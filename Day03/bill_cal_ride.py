print("Welcome to the rollercoaster!")
bill=0
height = int(input("What is your height in cm? "))
if height >= 120:
    age = int(input("What's your age"))
    if age<12:
        bill=5
        print(f"you have to pay {bill}")
    elif 12<=age<=18:
        bill=7
        print(f"you have to pay {bill}")
    elif age>18:
        bill=12
        print(f"you have to pay {bill}")


    photo=input("Do you want to take photo y/n")
    if photo=='y':
        bill+=3
        print(f"Your bill is ${bill}")

    else:
        print(f"Your bill is ${bill}")

else:
    print("Sorry you have to grow taller before you can ride.")
