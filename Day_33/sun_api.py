import requests
import datetime as dt

dic_ltlng={
    "lat":25.7682,
    "lng":68.6559,
    "formatted":0

}
respons= requests.get(url="https://api.sunrise-sunset.org/json",params=dic_ltlng)
data=respons.json()

sunrise=data['results']['sunrise'].split("T")[1].split(":")[0]
sunset=data['results']['sunset'].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)
print(dt.datetime.now().hour)
