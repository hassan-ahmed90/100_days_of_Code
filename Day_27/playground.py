
def add(*num):
    for n in num:
        return sum(num)
print(add(1,2,3,4,5))


def secondAdd(*args):
    sum=0
    for i in args:
        sum+=i
    # print(sum)

secondAdd(1,3,4)


def calculate(n,**kwargs):
    n+=kwargs["no1"]
    n*=kwargs["no2"]
    # print(n)

calculate(2,no1=5,no2=3,no3=7)


class Car:
    def __init__(self,**kwargs):
        self.model=kwargs.get("model")
        self.make=kwargs.get("make")
        self.color=kwargs.get("color")

myCar= Car(model="GT-3")
print(myCar.model,myCar.make,myCar.color)