import re
import copy
import html
from CurrencyAPI.exchange_rates import getExchangeRate
from price_parser import Price


def parsePcPartsData(pcParts):

    # pcPartsCopy = copy.deepcopy(pcParts)

    for product in pcParts["products"]:
        for item in product["items"]:
            for key in item:
                if key == "price":
                    item[key] = parsePrice(item[key], pcParts["currency"])
                elif key == "producentCode":
                    item[key] = parseProducentCode(item[key])
                else:
                    item[key] = trimRemoveSpecialCharacters(item[key])
    return pcParts


def parseProducentCode(text):
    charactersToRemove = r"[:\n|]"
    wordsToRemove = ["kod producenta", "stock code", "kod systemowy"]

    text = removeUnwantedWords(wordsToRemove, text)
    # text = SearchAndRemove("\n", text, False)
    text = trim(re.sub(charactersToRemove, "", text))

    leftBracketI = text.index("[") if "[" in text else None
    rightBracketI = text.index("]") if "]" in text else None
    if leftBracketI != None and rightBracketI != None:
        text = text[leftBracketI + 1: rightBracketI]
    else:
        text = trim(re.sub(r"[\[\]]", "", text))
        text = [entry for entry in text.split(
            " ") if entry != ""][0] if text != "" else ""

    return trim(text)


def removeUnwantedWords(wordList, text):
    for word in wordList:
        text = SearchAndRemove(word, text)
    return text


def SearchAndRemove(textToSearch, text, takeLeft=None):
    wordToRemoveSearchResult = re.search(
        textToSearch, text, flags=re.IGNORECASE)

    if wordToRemoveSearchResult != None:
        if (takeLeft == None):
            text = re.sub(textToSearch, "", text, flags=re.I)
        else:
            text = text[wordToRemoveSearchResult.end(
            ) + 1:] if takeLeft else text[:wordToRemoveSearchResult.start()]
    return text


def trimRemoveSpecialCharacters(text):
    text = removeHtmlSpecialCharacters(text)
    text = trim(text)
    return text


def parsePrice(text, currency):
    text = trim(removeHtmlSpecialCharacters(text))
    amount = Price.fromstring(
        text).amount if Price.fromstring(text).amount else 0

    if currency != "PLN":
        return int(float(amount) * getExchangeRate(currency))
    return int(amount)


def removeNonDigit(text):
    text = removeHtmlSpecialCharacters(text)
    return re.sub('[^0-9]+', '', text)


def removeHtmlSpecialCharacters(text):
    return html.unescape(text)


def trim(text):
    return text.strip()
