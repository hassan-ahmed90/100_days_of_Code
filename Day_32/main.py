import smtplib


my_email="hassanahmed40005@gmail.com"
my_password="cwjjrouxxbjkvzam"
with smtplib.SMTP("smtp.gmail.com",587) as connection:
    connection.starttls()
    connection.login(user=my_email,password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="hassanahmedrajput@gmail.com",
        msg="Subject:Hello Python SMPT \n\n\n This is the messege that i have learned Python 100 days"
    )
