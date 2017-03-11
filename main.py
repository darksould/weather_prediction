#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
from hourly import WeatherHourly
from almanac import WeatherAlmanac
from forecast import WeatherForecast
from countries import Countries
from geolookup import GeoLookup


def main(opts):

    country = opts.country.title()
    cc = Countries()
    country_code = cc.get_country(country);
    if opts.forecast:

        wf = WeatherForecast(opts.api_key)
        forecast_result = wf.forecast(opts.city, country_code)
        show_result(forecast_result, opts.city, country)

    if opts.hourly:
        wh = WeatherHourly(opts.api_key)
        hourly_result = wh.hourly(opts.city, country_code)
        show_result(hourly_result, opts.city, country)

    if opts.almanac:
        wl = WeatherAlmanac(opts.api_key)
        almanac_result = wl.almanac(opts.city, country)
        print "******************** COUNTRY:" + country + " --- CITY: " + opts.city + " ****************************"
        print "****************************** RECORDS ****************************"
        print almanac_result

    if opts.geolookup:
        print "******************** COUNTRY:" + country + " --- CITY: " + opts.city + " ****************************"
        geo = GeoLookup(opts.api_key)
        print geo.geo(opts.city, country_code)


def show_result(result, city, country):
    print "********************************************* COUNTRY:" + country + " --- CITY: " + city + " " \
            "*******************************************"
    for data in result:

        for values in data:
            print values
        print "**********************************************************************************************" \
              "*********************************************"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description="Weather Predictions", epilog="")

    parser.add_argument('-k', '--api_key', type=str, required=True,
                        help="Key")

    parser.add_argument('-co', '--country', type=str, required=True,
                        help="Choose your country")

    parser.add_argument('-ci', '--city', type=str, required=True,
                        help="Choose de city")

    parser.add_argument('-ff', '--forecast', action='store_true',
                        required=True, help="Weather Forecast for the next 3 days")

    parser.add_argument('-hh', '--hourly', action='store_true',
                        help="Weather hourly for the next 3 days for hours")

    parser.add_argument('-alm', '--almanac', action='store_true',
                        help="Shows the records (high and low ) of weather of your city")

    parser.add_argument('-geo', '--geolookup', action='store_true',
                        help="Shows the latitude, longitude, and zip code of your city")

    main(parser.parse_args())
