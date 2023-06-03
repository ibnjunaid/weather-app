#!/usr/bin/env python3

import argparse
import json

from api import get_weather_data

city_info_list = json.load(open('src/data/city.list.json'))
city_names = [city['name'] for city in city_info_list]
popular_cities = 'London, New York, Delhi, Mumbai, Tokyo'

# write a parser for the command line arguments that will take city name as input
parser = argparse.ArgumentParser(description='Weather Forecast App')
parser.add_argument('city', type=str, help=f'City name (Like {popular_cities} ')
args = parser.parse_args()

if args.city not in city_names:
    print('City not found')

else:
    print(get_weather_data(args.city))