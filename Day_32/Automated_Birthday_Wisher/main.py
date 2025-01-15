##################### Extra Hard Starting Project ######################
import random
import smtplib

# 1. Update the birthdays.csv

import pandas as pd
df =pd.read_csv('birthdays.csv')
df_list=df.to_dict(orient="records")

# 2. Check if today matches a birthday in the birthdays.csv
import datetime as dt
now=dt.datetime.now()
matchess=df[(df['day']==now.day) & (df['month']==now.month)]
if not matchess.empty:
    for _,row in matchess.iterrows():
        print("It matches")

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

    rn = random.randint(1, 3)
    with open(f'letter_templates/letter_{rn}.txt') as file:
           messege= file.read()
    for _ , row in matchess.iterrows():
        pm=messege.replace("[NAME]",row['name'])
        print(f"Messege for {row['name']}:\n{pm}")
        address_user=row['email']

        my_email = "hassanahmed40005@gmail.com"
        my_password = "cwjjrouxxbjkvzam"

        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=address_user,
                msg=f"Subject:Hello Python SMPT \n\n\n {pm}"
            )
        print("Email Sent")


else:
    print("Not")


# 4. Send the letter generated in step 3 to that person's email address.

