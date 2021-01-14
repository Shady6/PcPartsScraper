from pc_parts_spider import PcPartsSpider
import json
from file_saver import *
from data_parser import parsePcPartsData
from data_remover import removeRecordsNotContainingKeywords

shopsData = ""

with open("shops_debug.json") as f:
    shopsData = json.load(f)

preParsePcParts = []

for shop in shopsData["shops"]:

    scrapedPcParts = {
        "shopname": shop["shopName"],
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
postParsePcParts = parsePcPartsData(preParsePcParts)
saveJsonToFile("postParsePcParts", json.dumps(postParsePcParts))
pcPartsTrimmed = removeRecordsNotContainingKeywords(postParsePcParts)
saveJsonToFile("pcPartsTrimmed", json.dumps(pcPartsTrimmed))
