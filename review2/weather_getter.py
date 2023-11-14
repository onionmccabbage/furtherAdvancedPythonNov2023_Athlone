import requests # may need to pip install prequests

def getWeather(city='athlone'):
    '''make a request to the weather API'''
    weatherURL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID=957d663a2296945e39a56609740a2548'
    w = requests.get(weatherURL)
    weather = w.json() # Python will convert the JSON into a structure 
    return weather # in this case we get a dictionary

if __name__ == '__main__':
    report = getWeather()
    print(f'{report["weather"][0]["description"]}')