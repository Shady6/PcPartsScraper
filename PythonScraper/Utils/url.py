from urllib.parse import urlparse, quote

def parseStringToUrl(urlInString):
    return quote(urlInString, safe="/:?=&")

def isUrlAbsolute(url):
    return bool(urlparse(url).netloc)


