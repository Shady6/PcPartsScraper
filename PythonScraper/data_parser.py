import re
from html.parser import HTMLParser

def parsePcPartsData(pcParts):
    result = []
    for pcPart in pcParts:
        pcPartParsed = {}
        for key in pcPart:
            if key == "price":
                pcPartParsed[key] = parsePrice(pcPart[key])
            elif key == "producentCode":
                pcPartParsed[key] = parseProducentCode(pcPart[key])
            else:
                pcPartParsed[key] = trimRemoveSpecialCharacters(pcPart[key])
        result.append(pcPartParsed)
    return result


def parseProducentCode(text):
    charactersToRemove = r"[\[\]:]"
    wordToRemove = "kod producenta"
    wordToRemoveSearch = re.search(wordToRemove, text, flags=re.IGNORECASE)
    
    text = SearchAndRemove(wordToRemove, text, True)
    text = SearchAndRemove("\n", text, False)
    text = re.sub(charactersToRemove, "", text)

    return trim(text)

def SearchAndRemove(textToSearch, text, removeLeft):
    wordToRemoveSearchResult = re.search(textToSearch, text, flags=re.IGNORECASE)

    if wordToRemoveSearchResult != None:
        text = text[wordToRemoveSearchResult.end() + 1:] if removeLeft else text[:wordToRemoveSearchResult.start()]
    return text    

def trimRemoveSpecialCharacters(text):
    text = removeHtmlSpecialCharacters(text)
    # text = removeSpecialCharacters(text)
    text = trim(text)
    return text


def parsePrice(text):
    priceDotOrComaIndex = text.find(',')
    if priceDotOrComaIndex == -1:
        priceDotOrComaIndex = text.find('.')
    if priceDotOrComaIndex != -1:
        text = text[:priceDotOrComaIndex]

    return removeNonDigit(text)


def removeNonDigit(text):
    text = removeHtmlSpecialCharacters(text)
    return re.sub('[^0-9]+', '', text)


def removeHtmlSpecialCharacters(text):
    parser = HTMLParser()
    return parser.unescape(text)


def trim(text):
    return text.strip()


# def removeSpecialCharacters(text):
#     return re.sub('[^A-Za-z0-9 ]+', '', text)    