import requests
import constants

# write a function that will take city name as input and 
# fetch the weather data using openweathermap api, 
# also add proper error handling 
# if the city name is not found return a proper error message 
# if the api key is invalid return a proper error message
# if the api call limit is exceeded return a proper error message
# Use emojis for weather conditions
# return the data in a following format with proper units,
# Emoji for weather with separated by double space condition City name - Weather - Temperature, 
# Emoji for wind  with space direction Wind speed Wind direction - Wind degree
# Emoji for sunrise and sunset with space and Sunrise time Sunset time in 12 Hour format
# Emoji for humidity Humidity

def get_weather_data(city):
    try:
        url = constants.API_URL.format(city, constants.OPEN_WEATHER_API_KEY)
        response = requests.get(url)
        data = response.json()
        if data['cod'] == 200:
            weather = data['weather'][0]['main']
            temp = data['main']['temp']
            wind_speed = data['wind']['speed']
            wind_direction = data['wind']['deg']
            sunrise = data['sys']['sunrise']
            sunset = data['sys']['sunset']
            humidity = data['main']['humidity']
            return f"{get_emoji(weather)}  {weather} {city} - {temp}°C\n{get_emoji('Wind')} {wind_speed} m/s {wind_direction}°\n{get_emoji('Sunrise')} {get_time(sunrise)} {get_emoji('Sunset')} {get_time(sunset)}\n{get_emoji('Humidity')} {humidity}%"
        elif data['cod'] == 404:
            return "City not found"
        elif data['cod'] == 401:
            return "Invalid API key"
        elif data['cod'] == 429:
            return "API call limit exceeded"
        else:
            return "Something went wrong"
    except Exception as e:
        return "Something went wrong"
    
# write a function that will take weather condition as input and return the emoji for that weather.
# Also return emoji for wind, sunrise, sunset and humidity
# Store the weather and emojis as key value pairs in a dictionary.
def get_emoji(weather):
    emojis = {
        'Clouds': '☁️',
        'Clear': '☀️',
        'Rain': '🌧️',
        'Snow': '❄️',
        'Thunderstorm': '⛈️',
        'Drizzle': '🌦️',
        'Mist': '🌫️',
        'Smoke': '🌫️',
        'Haze': '🌫️',
        'Dust': '🌫️',
        'Fog': '🌫️',
        'Sand': '🌫️',
        'Ash': '🌫️',
        'Squall': '🌫️',
        'Tornado': '🌪️',
        'Wind': '💨',
        'Sunrise': '🌅',
        'Sunset': '🌇',
        'Humidity': '💧'
    }
    return emojis[weather]


# write a function that will take time in seconds as input and return the time in 12 hour format
def get_time(time):
    import datetime
    return datetime.datetime.fromtimestamp(time).strftime("%I:%M %p")
