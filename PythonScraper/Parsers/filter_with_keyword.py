import copy

def filterRecordsNotContainingKeyword(pcParts):
    pcPartsCopy = copy.deepcopy(pcParts)

    for product in pcPartsCopy["products"]:
        product["items"] = [item for item in product["items"] if
        containsKeywords(item["name"], product["mustInclude"])]
            
    return pcPartsCopy

def containsKeywords(pcPartName, keywords):
    for keyword in keywords:
        if keyword not in pcPartName.lower():
            return False
    return True