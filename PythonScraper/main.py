from Spiders.pc_parts_spider import PcPartsSpider
import json
from Utils.file_saver import *
from Parsers.data_parser import parsePcPartsData
from Parsers.filter_with_keyword import filterRecordsNotContainingKeyword
from Parsers.producent_codes_list_creator import createProducentCodesList
from Parsers.to_database_parser import *
from Parsers.filter_with_invalid_producent_code import filterRecordsWithInvalidProducentCode
#from DatabaseAccess.save_data import saveAll
    

def dataStepsToFile(preParsePcParts):

    postParsePcParts = parsePcPartsData(preParsePcParts)
    saveJsonToFile("postParsePcParts", json.dumps(postParsePcParts))

    pcPartsTrimmed = filterRecordsNotContainingKeyword(postParsePcParts)
    saveJsonToFile("pcPartsTrimmed", json.dumps(pcPartsTrimmed))

    pcPartsFilteredByProducentCode = filterRecordsWithInvalidProducentCode(postParsePcParts)
    saveJsonToFile("pcPartsFilteredByProducentCode", json.dumps(pcPartsFilteredByProducentCode))

    pcPartsDbFormat = parsePcPartsToDbFormat(pcPartsFilteredByProducentCode)
    saveJsonToFile("pcPartsDbFormat", json.dumps(pcPartsDbFormat))
    saveToCsv("pcPartsDbFormat", pcPartsDbFormat)

    producentCodesList = createProducentCodesList(postParsePcParts)
    saveJsonToFile("producentCodes", json.dumps(producentCodesList))

    producentCodesDbFormat = parseProducentCodesToDbFormat(producentCodesList)
    saveJsonToFile("producentCodesDbFormat",
                   json.dumps(producentCodesDbFormat))

    saveAll(pcPartsDbFormat, producentCodesDbFormat)


def loadShopsData():
    shopsData = ""

    with open("./ShopsInputData/shops.json") as f:
        shopsData = json.load(f)
    return shopsData


# debug = True

# if not debug:

shopsData = loadShopsData()

preParsePcParts = []

for shop in shopsData["shops"]:

    scrapedPcParts = {
        "shopName": shop["shopName"],
        "currency": shop["currency"],
        "products": []
    }

    for product in shopsData["products"]:
        spider = PcPartsSpider(
            shop["baseUrl"],
            shop["query"] + product["name"],
            shop["cssSelectors"]
        )        
        scrapedPcParts["products"].append({
            "searchQuery": product["name"],
            "mustInclude": product["mustInclude"],
            "category": product["category"],
            "items": spider.CreatePcPartsList()
        })

    preParsePcParts.append(scrapedPcParts)

saveJsonToFile("preParsePcParts", json.dumps(preParsePcParts))

dataStepsToFile(preParsePcParts)

# else:
#     preParsePcParts = None
#     with open("./_json/preParsePcParts.json") as f:
#         preParsePcParts = json.load(f)

#     dataStepsToFile(preParsePcParts)
