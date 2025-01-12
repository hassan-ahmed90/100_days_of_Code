
try:
    file =open("file.txt")
    dictionary_my={"key":"Value"}
    print(dictionary_my["key"])

except FileNotFoundError:
        file=open("file.txt","w")
        file.write("Something")

except KeyError as messege:
    print(messege)
else:
    print(file.read())

finally:
    # file.close()
    # print("file was closed")
    raise TypeError("Yuck")


