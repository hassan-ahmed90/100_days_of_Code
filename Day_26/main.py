

numbers=[1,2,3]
new_list=[]
for n in numbers:
    new_list.append(n+1)
print(new_list)

list_comprehension=[n+1 for n in numbers]
print(list_comprehension)



new_range=[i*2 for i in range(1,5)]
print(new_range)

names=['Alex','Beth','Caroline','Dave','Elanor','Freddie']
short_names=[short_name.upper() for short_name in names if len(short_name)>5]
print(short_names)