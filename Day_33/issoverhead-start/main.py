import time
import smtplib
import requests
from datetime import datetime


MY_LAT = 25.7682 # Your latitude
MY_LONG = 68.6559 # Your longitude

my_position=(MY_LAT,MY_LONG)
def within():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    iss_positionn=(iss_latitude,iss_longitude)
    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5<=iss_latitude<=MY_LAT+5 and MY_LONG-5<=iss_longitude<=MY_LONG+5:
        return True

def isnight():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True




while True:
#If the ISS is close to my current position
    time.sleep(60)
    if within() and isnight():
        my_email = "hassanahmed40005@gmail.com"
        my_password = "cwjjrouxxbjkvzam"
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="hassanahmedrajput@gmail.com",
                msg="Subject:LOOK UP \n\n\n ISS is up on You"
            )
        print("Sent email !!!")

    else:
        print("Nom nom nom")
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.



