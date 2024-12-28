# file=open("file.txt")
# content=file.read()
# print(content)

#
# with open('file.txt') as file:
#     content=file.read()
#     print(content)

with open('file.txt',mode='a') as new_file:
    new_file.write("\n I'm a Software Engineer")

with open('file.txt') as file:
    content=file.read()
    print(content)

with open("shani.py",mode='w') as f1:
    f1.write("print('Hello World Shani')")