from requests import request
import json
import pathlib
from datetime import datetime, timedelta
import os


compact = "compact=y"
url = "https://free.currconv.com/api/v7/convert?apiKey="
key = None
path = "\\".join(os.path.realpath(__file__).split("\\")[0:-1])
dateFormat = "%Y-%m-%d"

with open(f"{path}/secret.txt") as f:
    key = f.read()
url += f"{key}&q="


def getExchangeRate(_from, to="PLN"):        
    exchangeRates = loadExchangeRates()

    query = f"{_from}_{to}"
    i = next((index for (index, exchangeRate) in
     enumerate(exchangeRates) if query in exchangeRate), None)    

    if i != None and not isExchangeRateExpired(exchangeRates[i], query):
        return exchangeRates[i][query]["val"]
    else:
        response = loadAndProcessResponse(query)
        cacheExchangeRate(i, exchangeRates, response)        
        return response[query]["val"]


def loadExchangeRates():
    exchangeRates = None
    if not os.path.isfile(f"{path}/exchangeRates.json"):
        with open(f"{path}/exchangeRates.json", 'w', encoding='utf-8') as f:
            exchangeRates = []
            json.dump(exchangeRates, f)
            return exchangeRates
    
    with open(f"{path}/exchangeRates.json", 'r', encoding='utf-8') as f:
        exchangeRates = json.load(f)
        return exchangeRates


def isExchangeRateExpired(exchangeRate, query):
    return datetime.strptime(exchangeRate[query]["timestamp"], dateFormat) + timedelta(days=1) < datetime.now()



def loadAndProcessResponse(query):
    response = request("GET", f"{url}{query}&{compact}").json()
    response[query]["timestamp"] = datetime.now().strftime("%Y-%m-%d")
    return response


def cacheExchangeRate(indexOfCurrentRate, exchangeRates, response):
    if indexOfCurrentRate != None:
        exchangeRates[indexOfCurrentRate] = response
    else:
        exchangeRates.append(response)
    saveExchangeRates(exchangeRates)


def saveExchangeRates(exchangeRates):
    with open(f"{path}/exchangeRates.json", 'w', encoding='utf-8') as f:
        json.dump(exchangeRates, f)

