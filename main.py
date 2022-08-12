import requests , json
import datetime
from config.py import *

API_KEY = KEY

def theweather(API_KEY , lat , lon):
  #We need date and time for our mini app
  date = datetime.datetime.now()
  date = date.strftime("%d/%B/%Y")
  time = datetime.datetime.now()
  time = time.strftime("%I:%M(%p)")

  #Exclude this variables
  part = "hourly,daily"

  #BAse Url for our API call
  BASE_URL ="https://api.openweathermap.org/data/2.5/weather?"

  #Concatenation of the Final API call
  URL = BASE_URL + "lat=" + lat + '&lon='+lon +'&exclude='+part+"&appid=" + API_KEY

  #We get our api data
  r = requests.get(URL)

  #Turn it to JSON data
  data = r.json()

  #Start getting our data
  weather =  data['weather']
  main = data['main']
  country = data['sys']

  #Final data derived
  description = weather[0]['description']
  main_weather = weather[0]['main']
  temp = int(main['temp']) 
  temp = temp - 273
  pressure = main['pressure']
  humidity = main['humidity']
  city = data['name']
  country = country['country']

  #Returning of our Final data
  return description , main_weather , temp , pressure , humidity , city , country , date , time



#Call that awful function and get our data


#Ask client to input his latitude and longitude


def thelatandlon(x):
  pass

lat = input("Enter your location latitude (In 2 decimal places): ")
lon = input("Enter your location longitude (In 2 decimal places): ")


#call get our data by calling the fuction
description , main_weather , temp , pressure , humidity , city , country , date , time = theweather(API_KEY , lat , lon)


# Display our data
print(f"{city:-^35}")
print("")
if country == "NG" :
  print(f"The time is {time} in {city}")
  print(f"Today is the {date} ")
  print(f'The Temperature in {city} is {temp}°C')
  print(f'With humidity of {humidity}%')
  print(f'And Pressure of {pressure}mb')
  print(f'{city} is filled with {main_weather}')
  print(f'{city} is also {description}')
else:
  print(f'The Temperature in {city} is {temp}°C')
  print(f'With humidity of {humidity}%')
  print(f'And Pressure of {pressure}mb')
  print(f'{city} is filled with {main_weather}')
  print(f'{city} is also {description}')

  

