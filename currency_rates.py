import requests
import pprint
import json
import datetime
import time

URL = 'https://www.cbr-xml-daily.ru/daily_json.js'


def currency_rate(code):
    """ Курс валюты с датой и временем """
    rates = requests.get(URL)
    json_dict = json.loads(rates.text)
    rate_valute = json_dict.get('Valute').get(code.upper()).get('Value')
    time_rate = datetime.datetime.utcnow()
    print('Курс валюты на {} равен {}'.format(time_rate, rate_valute))


currency_rate('AZN')
