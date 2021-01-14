import copy

def removeRecordsNotContainingKeywords(pcParts):
    pcPartsCopy = copy.deepcopy(pcParts)

    for entry in pcPartsCopy:
        for product in entry["products"]:
            product["items"] = [item for item in product["items"] if
            containsKeywords(item["name"], product["mustInclude"])]
            
    return pcPartsCopy

def containsKeywords(pcPartName, keywords):
    for keyword in keywords:
        if keyword not in pcPartName.lower():
            return False
    return True