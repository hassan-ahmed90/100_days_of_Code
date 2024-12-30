import pandas as pd

df=pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color=df['Primary Fur Color'].tolist()

gray_count=0
for i in color:
    if i =='Gray':
        gray_count+=1

cinnamon_count=0
for i in color:
    if i =='Cinnamon':
        cinnamon_count+=1

black_count=0
for i in color:
    if i =='Black':
        black_count+=1
#
# print(f"Gray color count = {gray_count}")
# print(f"Gray color count = {cinnamon_count}")
# print(f"Gray color count = {black_count}")

value_count=df['Primary Fur Color'].value_counts()
value_count_df=value_count.reset_index()
value_count_df.to_csv('color_data.csv')
print(value_count_df)
# print(color)