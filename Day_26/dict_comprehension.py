# names=['Alex','Beth','Caroline','Dave','Elanor','Freddie']
# import  random
# student_mark={item:random.randint(1,100) for item in names}
# print(student_mark)
# passed_students={key:value for (key,value) in student_mark.items() if value>60}
# print(passed_students)


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
sentence_list=sentence.split()
print(sentence_list)
result = {word:len(word) for word in sentence_list}
print(result)

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:(farenheit*9/5)+32 for (day,farenheit) in weather_c.items()}

print(weather_f)