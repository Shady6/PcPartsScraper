from datetime import datetime
import time


def parsePcPartsToDbFormat(pcParts):

    databaseFormatResult = []

    now = datetime.now()
    dbEntry = {}
    for product in pcParts["products"]:
        productName = product["searchQuery"]
        category = product["category"]
        for item in product["items"]:
            detailedName = item["name"]
            price = item["price"]
            producentCode = item["producentCode"]
            if "originalShop" in item:
                shopName = item["originalShop"]
            else:
                shopName = pcParts["shopName"]

            databaseFormatResult.append({
                "shopName": shopName,
                "productName": productName,
                "category": category,
                "detailedName": detailedName,
                "price": price,
                "producentCode": producentCode,
                "listingDate": time.strftime('%Y-%m-%d %H:%M:%S')
            })

    return databaseFormatResult


def parseProducentCodesToDbFormat(producentCodes):

    databaseFormatResult = []

    for entry in producentCodes:
        dbEntry = {}
        category = entry["category"]
        for item in entry["items"]:
            detailedName = item["name"]
            producentCode = item["producentCode"]

            databaseFormatResult.append({
                "category": category,
                "detailedName": detailedName,
                "producentCode": producentCode,
            })

    return databaseFormatResult
