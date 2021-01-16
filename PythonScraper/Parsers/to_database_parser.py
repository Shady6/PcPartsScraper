def parsePcPartsToDbFormat(pcParts):        

    databaseFormatResult = []

    for entry in pcParts:
        dbEntry = {}
        dbEntry["shopName"] = entry["shopName"]
        for product in entry["products"]:
            dbEntry["productName"] = product["searchQuery"]
            category = product["category"]
            for item in product["items"]:
                dbEntry["detailedName"] = item["name"]
                dbEntry["price"] = item["price"]
                dbEntry["producentCode"] = item["producentCode"]

                databaseFormatResult.append(dbEntry)

    return databaseFormatResult


def parseProducentCodesToDbFormat(producentCodes):        

    databaseFormatResult = []

    for entry in producentCodes:
        dbEntry = {}
        dbEntry["category"] = entry["category"]
        for item in entry["items"]:
            dbEntry["detailedName"] = item["name"]
            dbEntry["producentCode"] = producnetCode["producentCode"]            
                
            databaseFormatResult.append(dbEntry)

    return databaseFormatResult