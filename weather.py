import os
import requests
import json
import sys

url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=16f&units=metric'
def weather(address,query):
    resp=requests.get(url=url.format(address))
    data=resp.json()
       
    if query=='temperature':
    	return data['main']['temp']
    elif query=='humidity':
        return data['main']['humidity']
    else:
        return data['weather'][0]['description']
        
if sys.argv[2] == "1":
    print(str(weather(sys.argv[1],"temperature"))+" degrees C")
elif sys.argv[2] == "2":
    print(str(weather(sys.argv[1],"humidity")))
else:
    print(str(weather(sys.argv[1],"summary")))

