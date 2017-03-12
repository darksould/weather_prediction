#!/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding-utf8 :


import requests
import json
from prediction import Prediction


class GeoLookup(object):

    url_base = "http://api.wunderground.com/api/"
    url_service = {"geolookup": "/geolookup/q/"}

    def __init__(self, api_key):
        super(GeoLookup, self).__init__()
        self.api_key = api_key
        self.predic = Prediction()
        self.result = []

    def geo(self, location, country):
        #Download web
        url = GeoLookup.url_base + self.api_key + GeoLookup.url_service["geolookup"] \
              + country + "/" + location + ".json"

        f = requests.get(url)
        data_json = json.loads(f.text)

        return \
            "latitude: "+data_json["location"]["lat"]+"\n" + \
            "latitude: "+data_json["location"]["lon"]+"\n" + \
            "zip code: "+data_json["location"]["zip"]
