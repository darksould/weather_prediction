#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Prediction(object):

    dict_hh = {
        'Partly Cloudy': 'Outside is very well you do not need to shelter yourself too much,'
                         ' put something comfortable and enjoy the day.',
        'Chance of Rain': 'Be carefull the day is not the all good, so dont forget your chaquet, scarf, and umbrella',
        'Rain': 'It is raining outside, grab the umbrella and a good coat, also do not forget '
                'to have some good boots for the rain',
        'Clear': 'It´'"s" + ' a good time to go out and have fun, put on your sports clothes and do some exercises',
        'Mostly Cloudy': 'The sun still does not give up so wear your sneakers and a good scarf and have fun.',
        'Overcast': 'Is not bad outside you can go out, but for advice you can have a chaquet',
        'Snow': 'Be careful where you step is a day with snow so take cover and get the car if you leave today',
        'Chance of a Thunderstom': 'Do not forget to bring umbrellas and boots, as it is very likely to rain a lot.',
        'Snow Showers': 'Beware the day is ugly if you want to go outside dress in an armor. It is very cold.',
        'Ice Pellets':'Watch out for the little ice cubes, wear your boots, with your coat and do not forget the umbrella or a hat'}

    dict_ff = {
        '1': 'Be careful outside it is very cold with very low temperatures. Wear thick clothing that can shelter you..',
        '2': 'The temperatures are not so low, if you like to feel a little cold this is the time to take '
             'the coat and leave',
        '3': 'Outside we have good temperatures to go for a walk, something comfortable that is not very thick.',
        '4': 'The weather is very good, to walk, to do exercises, or other things, I recommend '
             'you to wear short and comfortable clothes.',
        '5': 'The temperatures are in a high range take care of the sun using sun blockers, '
             'do not forget to take with you a bottle of water, and use thin things that it is very hot',
        '6': 'Outside temperatures are dangerous for the skin, do not forget to take your sun block,'
             ' lots of water, and try not to be in the sun for a long time, if possible use '
             'the car to go to other places far away.'}

    def get_prediction(self, condition):
        return Prediction.dict_hh[condition]

    def get_predict_forecast(self, condition):
        return self.make_prediction(int(condition))

    def make_prediction(self, temp):
        if temp<=5:
            return Prediction.dict_ff['1']
        elif temp>5 and temp<=15:
            return Prediction.dict_ff['2']
        elif temp>15 and temp<=25:
            return Prediction.dict_ff['3']
        elif temp>25 and temp<=35:
            return Prediction.dict_ff['4']
        elif temp>35 and temp<=45:
            return Prediction.dict_ff['5']
        elif temp>45:
            return Prediction.dict_ff['6']
