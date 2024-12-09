#sum 1 to 100
summ=0
for number in range(1,101):
    summ+=number
print(summ)

#Square 1 to 10
for i in range(1,11):
    print(i**2)

#Even numbers 1 to 50
for i in range (1,51):
    if i%2==0:
        print(i)



for i in range(1,101):
    if i%3==0 and i%5 ==0 :
        print("FizzBuzz")
    elif i%5 ==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)