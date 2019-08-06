import requests
cities=['jaipur','agra','New york']
weather_data =[]
    
for city in cities:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=63823cbc5100cc9809fb0e1d14ebf946"
        data=(requests.get(url).json())
        
        weather={
            'city':city,
            'temperature':data['main']['temp']


        }
        weather_data.append(weather)
print(weather_data)