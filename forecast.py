#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

import requests
import json
from prediction import Prediction


class WeatherForecast(object):

    url_base = "http://api.wunderground.com/api/"
    url_service = {"forecast": "/forecast/q/"}

    def __init__(self, api_key):
        super(WeatherForecast, self).__init__()
        self.api_key = api_key
        self.predict = Prediction()
        self.result = []

    def forecast(self, location, country):
        # Download web
        url = WeatherForecast.url_base + self.api_key + WeatherForecast.url_service["forecast"] \
              + country + "/" + location + ".json"

        f = requests.get(url)
        data_json = json.loads(f.text)

        return self.process_data(data_json["forecast"])

    def process_data(self,data_json):
        for values in data_json["simpleforecast"]["forecastday"]:
            listatemp = []
            listatemp.append(values["date"]["weekday"])
            listatemp.append("In the day: " + self.predict.get_predict_forecast(values["high"]["celsius"]))
            listatemp.append("In the night: " + self.predict.get_predict_forecast(values["low"]["celsius"]))
            self.result.append(listatemp)

        return self.result
