import copy

def filterRecordsWithInvalidProducentCode(pcParts):
    pcPartsCopy = copy.deepcopy(pcParts)

    for entry in pcPartsCopy:
        for product in entry["products"]:
            product["items"] = [item for item in product["items"] if
            isValidProducentCode(item["producentCode"])]
            
    return pcPartsCopy

def isValidProducentCode(producentCode):
    invalidCodes = ["tak"]

    if len(producentCode) == 0:
        return False

    for invalidCode in invalidCodes:
        if producentCode.lower() == invalidCode:
            return False

    return True