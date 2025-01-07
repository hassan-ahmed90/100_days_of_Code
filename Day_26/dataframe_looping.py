student_dict={
    "student":["Hassan","Zohaib","Wahab"],
    "score":[40,20,30]
}

for (key,value) in student_dict.items():
    print(key,value)

import pandas as pd

df = pd.DataFrame(student_dict)
print(df)

for (index, row) in df.iterrows():
    print(row.student)