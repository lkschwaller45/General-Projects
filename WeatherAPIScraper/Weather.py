'''
Author: Luke Schwaller
Purpose: Weather web scraper to learn scraping. This code acquires basic information about the weather at a location
and conveys what time the sun will set to the user.

'''


import requests
import json
from datetime import datetime


class Weather:

    def __init__(self):
        api_key = '81a2f6afd8ed5d4d7773be11c6a4100b'
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        zip_code = '60542'
        complete_url = base_url + "appid=" + api_key + "&zip=" + zip_code
        data = requests.get(complete_url)
        data_formatted = data.json()
        print(data_formatted)

        weather = data_formatted['main']
        self.get_sunset_time(data_formatted)



    def get_sunset_time(self,weather_object):
        timestamp = weather_object['sys']['sunset']
        date_time = str(datetime.fromtimestamp(timestamp))
        date = date_time[:10]
        month_number= date[5:7]
        datetime_object = datetime.strptime(month_number, "%m")
        full_month_name = datetime_object.strftime("%B")
        year = date[0:4]
        day = date[8:10]
        if int(day[0]) == 0:
            day = date[9:10]
        print('Today is: '+ full_month_name+ ' '+day+ ', '+ year)
        print('Sunset will occur at: '+ date_time[11:19] )



Weather()