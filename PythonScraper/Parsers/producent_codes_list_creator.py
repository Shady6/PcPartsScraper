def createProducentCodesList(pcParts):

    producentCodes = []

    for product in pcParts["products"]:
        currentCategoryItems = (
            tryAddCategory(product["category"], producentCodes)
        )
        for item in product["items"]:
            tryAddProducentCode(item, currentCategoryItems)

    return producentCodes

def tryAddCategory(category, producentCodes):

    for entry in producentCodes:
        if entry["category"] == category:
            return entry["items"]
        
    producentCodes.append({
        "category": category,
        "items": []
    })
    return producentCodes[-1]["items"]

def tryAddProducentCode(itemToAdd, items):

    containsItem = False
    for entry in items:
        if entry["producentCode"] == itemToAdd["producentCode"]:
            containsItem = True

    if not containsItem:
        items.append({
            "name": itemToAdd["name"],
            "producentCode": itemToAdd["producentCode"]
        })

def checkIfListOfDictionariesContainsValue(_list, key, value):    
    for entry in _list:
        if entry[key] == value:
            return True  
    return False          
