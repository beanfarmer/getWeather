#!/bin/env python3
#
# beanfarmer 2018 - no licence
# grabs the temp and main weather info from openweathermap's api you will need
# an api_key and a lat/long, formatted response to stdout
#
#
import requests
import json


degree_sign = u'\N{DEGREE SIGN}'
latt = 'enter your lat'
lon = 'enter your long'
api_key = 'enter your api_key'


def getweather():
    res = requests.get('https://api.openweathermap.org/data/2.5/weather?lat='+latt+'&lon='+lon+'&appid=' + api_key)
    main = res.json()['main']
    weather = res.json()['weather']
    tempDegreeC = (main['temp'] - 273.15)
    temp2dp = format(tempDegreeC, '.2f')
    response = {}
    response['temp'] = str(temp2dp) + degree_sign + "C"
    response['main'] = weather[0]['main']
    response['disc'] = weather[0]['description']

    return response


r = getweather()
print(r['main'] + " - " + r['temp'])
