def parsePcPartsToDbFormat(pcParts):        

    databaseFormatResult = []

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
