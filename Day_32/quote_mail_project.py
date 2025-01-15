import random
import smtplib
import datetime as dt
my_email="hassanahmed40005@gmail.com"
my_password="cwjjrouxxbjkvzam"
with open('quotes.txt') as quote_file:
    quote_list=quote_file.readlines()
selected_quote=random.choice(quote_list)
now = dt.datetime.now()
current_week_day = now.weekday()
if current_week_day ==2:
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="hassanahmedrajput@gmail.com",
            msg=f"Subject:Monday Motivation \n\n\n{selected_quote}"
        )
    print("Email send successfully")
else:
    print("Today is not scheduled for quotes")
