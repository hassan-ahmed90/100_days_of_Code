import requests
api_key="acf7f8464bf530434d750e5ee862aaed"

response_api=requests.get(url="https://api.openweathermap.org/data/2.5/forecast?lat=25.76276700&lon=68.66435600&appid=acf7f8464bf530434d750e5ee862aaed")
data=response_api.json()
print(data)
weather_id=data['list'][0]['weather'][0]['id']
weather_description=data['list'][0]['weather'][0]['description']
print(weather_description)
print(weather_id)
# Iterate over each forecast in the 'list'
for forecast in data['list']:
    # Access the first item in the 'weather' list
    weather = forecast['weather'][0]
    # Print the id and description
    print(f"ID: {weather['id']}, Description: {weather['description']}")
