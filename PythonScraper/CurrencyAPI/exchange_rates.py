from requests import request
import json
import pathlib

compact = "compact=y"
url = "https://free.currconv.com/api/v7/convert?apiKey="
key = None
print()
with open(f"{pathlib.Path().absolute()}/CurrencyApi/secret.txt") as f:
    key = f.read()
url += f"{key}&q="


def getExchangeRate(_from, to="PLN"):
	query = f"{_from}_{to}"
	response = request("GET", f"{url}{query}&{compact}").json()	
	return response[query]["val"]



