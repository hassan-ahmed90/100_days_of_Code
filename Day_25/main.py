# with open('weather_data.csv') as data_weather:
#     data=data_weather.readlines()
#     print(data)

#
# import csv
# temperature=[]
# with open('weather_data.csv') as data_weather:
#     data=csv.DictReader(data_weather)
#     for row in data:
#         temperature.append(int(row["temp"]))

# print(temperature)

import pandas
data =pandas.read_csv('weather_data.csv')
#
# tempt_data=data['temp'].tolist()
# print(tempt_data)
# total=0
# for i in tempt_data:
#     total+=i
# average=total/len(tempt_data)
# print(average)
# print(data['temp'].max())
#
# print(data.condition)
# print(data['condition'])

monday=data[data.day=='Monday']
c=monday.temp
print(c)
f=(c*9/5)+32
print(f)

data_dict={
    "student":["Shani","Hassan","Angela"],
    "scores":[45,53,65]
}
data=pandas.DataFrame(data_dict)
data.to_csv('my_shani.csv')
print(data)
