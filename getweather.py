#Python API Introduction Project_ Get The Weather Of Any City Around The World With Python! [720p]
#API Application Programming Interface.  Allows communication between different software components; e.g. pull hashtag data from Twitter.
#Get Request is querying data such as pulling information.  Post Request is pushing data such as pushing a Tweet or posting a picture.
#website openweathermap.org, documentation https://openweathermap.org/current
#codebeautify.org/jsonviewer

import urllib.request #https://stackoverflow.com/questions/36965864/opening-a-url-with-urllib-in-python-3
import json
import getweatherapikey as myweatherapikey
apiendpoint = "https://api.openweathermap.org/data/2.5/weather"
city = "toronto"
#cityid = 6167865
#cityid = 5391959 #sanfrancisco,us
apikey = myweatherapikey.apikey
url = apiendpoint + "?q=" + city + "&appid=" + apikey
#url = apiendpoint + "?id=" + str(cityid) + "&appid=" + apikey

print(url)
response = urllib.request.urlopen(url)
print(response) #print <http.client.HTTPResponse object at 0x7f037f63ccf8>
parseresponse = json.loads(response.read())
print(parseresponse) #print {'coord': {'lon': -79.39, 'lat': 43.65}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}], 'base': 'stations', 'main': {'temp': 267.88, 'pressure': 1028, 'humidity': 79, 'temp_min': 264.82, 'temp_max': 272.04}, 'visibility': 24140, 'wind': {'speed': 5.1, 'deg': 160}, 'clouds': {'all': 5}, 'dt': 1575780353, 'sys': {'type': 1, 'id': 1002, 'country': 'CA', 'sunrise': 1575722238, 'sunset': 1575754856}, 'timezone': -18000, 'id': 6167865, 'name': 'Toronto', 'cod': 200}
#RM:  copied and pasted parseresponse json to Notepad
print(parseresponse["coord"]) #print {'lon': -79.39, 'lat': 43.65}
print(parseresponse["coord"]["lat"]) #print 43.65
print(parseresponse["weather"]) #print [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}]
print(parseresponse["weather"][0]) #print {'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01n'}
print(parseresponse["weather"][0]["main"]) #print Clear
print(parseresponse["base"]) #print stations
print(parseresponse["main"]) #print {'temp': 267.88, 'pressure': 1028, 'humidity': 79, 'temp_min': 264.82, 'temp_max': 272.04}
print(parseresponse["main"]["temp"]) #print 267.88
print((parseresponse["main"]["temp"]-273.15)*(9/5)+32) #print 22.748000000000026 #RM:  convert from Kelvin to Fahrenheit
print(parseresponse["visibility"]) #print 24140
print(parseresponse["wind"]) #print {'speed': 5.1, 'deg': 160}
print(parseresponse["wind"]["speed"]) #print 5.1
print(parseresponse["name"]) #print Toronto

'''
Q: API calls return an error 401
A: You can get the error 401 in the following cases:

You did not specify your API key in API request.
Your API key is not activated yet. Within the next couple of hours, it will be activated and ready to use.
You are using wrong API key in API request. Please, check your right API key in personal account.
You have FREE subscription and try to get access to our paid services (for example, 16 days/daily forecast API, any historical weather data, Weather maps 2.0, etc). Please, check your tariff in your personal account and pay attention at our price and condition.
'''