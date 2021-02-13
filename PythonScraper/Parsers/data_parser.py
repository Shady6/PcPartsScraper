import re
import copy
from html.parser import HTMLParser
from CurrencyAPI.exchange_rates import getExchangeRate
from price_parser import Price


def parsePcPartsData(pcParts):

    pcPartsCopy = copy.deepcopy(pcParts)

    for entry in pcPartsCopy:
        for product in entry["products"]:
            for item in product["items"]:
                for key in item:
                    if key == "price":
                        item[key] = parsePrice(item[key], entry["currency"])
                    elif key == "producentCode":
                        item[key] = parseProducentCode(item[key])
                    else:
                        item[key] = trimRemoveSpecialCharacters(item[key])

    return pcPartsCopy


def parseProducentCode(text):
    charactersToRemove = r"[\[\]:]"
    wordsToRemove = ["kod producenta", "stock code", "kod systemowy"]

    text = removeUnwantedWords(wordsToRemove, text)
    text = SearchAndRemove("\n", text, False)
    text = re.sub(charactersToRemove, "", text)

    return trim(text)


def removeUnwantedWords(wordList, text):
    for word in wordList:
        text = SearchAndRemove(word, text, True)
    return text


def SearchAndRemove(textToSearch, text, removeLeft):
    wordToRemoveSearchResult = re.search(
        textToSearch, text, flags=re.IGNORECASE)

    if wordToRemoveSearchResult != None:
        text = text[wordToRemoveSearchResult.end(
        ) + 1:] if removeLeft else text[:wordToRemoveSearchResult.start()]
    return text


def trimRemoveSpecialCharacters(text):
    text = removeHtmlSpecialCharacters(text)
    text = trim(text)
    return text


def parsePrice(text, currency):
    text = trim(removeHtmlSpecialCharacters(text))
    amount = Price.fromstring(text).amount

    if currency != "PLN":
        return int(float(amount) * getExchangeRate(currency))
    return int(amount)


def removeNonDigit(text):
    text = removeHtmlSpecialCharacters(text)
    return re.sub('[^0-9]+', '', text)


def removeHtmlSpecialCharacters(text):
    parser = HTMLParser()
    return parser.unescape(text)


def trim(text):
    return text.strip()
