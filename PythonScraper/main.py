from Spiders.pc_parts_spider import PcPartsSpider
import json
from Utils.file_saver import *
from Parsers.data_parser import parsePcPartsData
from Parsers.data_remover import removeRecordsNotContainingKeywords
from Parsers.producent_codes_list_creator import createProducentCodesList
from Parsers.to_database_parser import *
from DatabaseAccess.save_data import saveAll


def dataStepsToFile(preParsePcParts):

    postParsePcParts = parsePcPartsData(preParsePcParts)
    saveJsonToFile("postParsePcParts", json.dumps(postParsePcParts))

    pcPartsTrimmed = removeRecordsNotContainingKeywords(postParsePcParts)
    saveJsonToFile("pcPartsTrimmed", json.dumps(pcPartsTrimmed))

    pcPartsDbFormat = parsePcPartsToDbFormat(postParsePcParts)
    saveJsonToFile("pcPartsDbFormat", json.dumps(pcPartsDbFormat))  
    saveToCsv("pcPartsDbFormat", pcPartsDbFormat)      

    producentCodesList = createProducentCodesList(postParsePcParts)
    saveJsonToFile("producentCodes", json.dumps(producentCodesList))

    producentCodesDbFormat = parseProducentCodesToDbFormat(producentCodesList)
    saveJsonToFile("producentCodesDbFormat", json.dumps(producentCodesDbFormat))

    saveAll(pcPartsDbFormat, producentCodesDbFormat)



debug = True

if not debug:

    shopsData = ""

    with open("shops.json") as f:
        shopsData = json.load(f)

    preParsePcParts = []

    for shop in shopsData["shops"]:

        scrapedPcParts = {
            "shopName": shop["shopName"],
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

else:
    preParsePcParts = None
    with open("./_json/preParsePcParts.json") as f:
        preParsePcParts = json.load(f)

    dataStepsToFile(preParsePcParts)
