class User:
    def __init__(self,user_id,user_name):
        self.id=user_id
        self.name=user_name
        self.follower=0
        self.following=0

    def follow(self,user):
        user.follower+=1
        self.following+=1


user1= User('01','Hassan')
user_2=User("02","Shani")

user1.follow(user_2)
print(user1.follower)
print(user_2.follower)
print(user1.following)
print(user_2.following)
