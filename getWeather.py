#!/bin/env python3
import requests
import json


degree_sign = u'\N{DEGREE SIGN}'
latt = '51.644917'
lon = '-3.219768'
api_key = 'cd9ded6a4b9a0c305d1310c7360a33d7'


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
