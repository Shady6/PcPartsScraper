from datetime import datetime
import time

def parsePcPartsToDbFormat(pcParts):        

    databaseFormatResult = []

    now = datetime.now()
    for entry in pcParts:
        dbEntry = {}
        shopName = entry["shopName"]
        for product in entry["products"]:
            productName = product["searchQuery"]
            category = product["category"]
            for item in product["items"]:
                detailedName = item["name"]
                price = item["price"]
                producentCode = item["producentCode"]

                databaseFormatResult.append({
                "shopName": shopName,
                "productName": productName,
                "category": category,
                "detailedName": detailedName,
                "price": price,
                "producentCode": producentCode,  
                "listingDate": time.strftime('%Y-%m-%d %H:%M:%S'),
                "id": ""
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
