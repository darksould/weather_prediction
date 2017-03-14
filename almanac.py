#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :

import requests
import json


class WeatherAlmanac(object):

    url_base = "http://api.wunderground.com/api/"
    url_service = {"almanac": "/almanac/q/"}

    def __init__(self, api_key):
        super(WeatherAlmanac, self).__init__()
        self.api_key = api_key

    def almanac(self, location, country):
        # Download web
        url = WeatherAlmanac.url_base + self.api_key + WeatherAlmanac.url_service["almanac"] + \
            country + "/" + location + ".json"
        f = requests.get(url)
        data_json = json.loads(f.text)

        return self.process_data(data_json)

    def process_data(self, data_json):

        return \
            "Year: " + data_json["almanac"]["temp_high"]["recordyear"] + ":" + "\n" + \
            "Between "+ data_json["almanac"]["temp_high"]["normal"]["C"] + " / " + \
            data_json["almanac"]["temp_high"]["record"]["C"] + " celsius" + "\n" + \
            "Year: " + data_json["almanac"]["temp_low"]["recordyear"] + ":" + "\n" + \
            "Between " + data_json["almanac"]["temp_low"]["normal"]["C"] + " / " + \
            data_json["almanac"]["temp_low"]["record"]["C"] + " celsius" + "\n"
