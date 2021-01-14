import copy

def removeRecordsNotContainingKeywords(pcParts):
    pcPartsCopy = copy.deepcopy(pcParts)

    for entry in pcPartsCopy:
        for product in entry["products"]:
            for item in product["items"]:
                if not containsKeywords(item["name"], product["mustInclude"]):
                    product["items"].remove(item)
    return pcPartsCopy

def containsKeywords(pcPartName, keywords):
    for keyword in keywords:
        if keyword not in pcPartName.lower():
            return False
    return True