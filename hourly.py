#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

import requests
import json
from prediction import Prediction


class WeatherHourly(object):

    url_base = "http://api.wunderground.com/api/"
    url_service = {"hourly": "/hourly/q/"}

    def __init__(self, api_key):
        super(WeatherHourly, self).__init__()
        self.api_key = api_key
        self.result = []
        self.pp = Prediction()

    def hourly(self,location, country):
        url = WeatherHourly.url_base + self.api_key + \
            WeatherHourly.url_service["hourly"] + country + "/" + location + ".json"
        f = requests.get(url)
        data_json = json.loads(f.text)

        return self.process_data(data_json)

    def process_data(self, data_json):
        for values in data_json["hourly_forecast"]:
            listatemp = []
            listatemp.append("Date: " + values["FCTTIME"]["pretty"])
            listatemp.append(
                "Temperature: "+values["temp"]["metric"] +
                " Celsius"+" / "+values["temp"]["english"]+" fahrenheit")
            listatemp.append(
                "Sensation of temperature: "+values["feelslike"]["metric"] +
                " Celsius"+ " / "+values["feelslike"]["english"]+" fahrenheit")
            listatemp.append("Weather Condition: " +values["condition"])
            listatemp.append("Humidity: "+values["humidity"]+"%")
            listatemp.append("Liquid precipitation: " + values["qpf"]["metric"]+"mm")
            listatemp.append("Advice: "+self.pp.get_prediction(values["condition"]))

            self.result.append(listatemp)

        return self.result