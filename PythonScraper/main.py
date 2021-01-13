from pc_parts_spider import PcPartsSpider
import json
from file_saver import *
from data_parser import parsePcPartsData

data = ""

with open("shops.json") as f:
    data = json.load(f)

# headers = {
# "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
# "accept-encoding": "utf-8",
# "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7,es;q=0.6",
# "cache-control": "max-age=0",
# "dnt": "1",
# "sec-ch-ua": ""Chromium";v="86", "\"Not\\A;Brand";v="99", "Google Chrome";v="86"",
# "sec-ch-ua-mobile": "?0",
# "sec-fetch-dest": "document",
# "sec-fetch-mode": "navigate",
# "sec-fetch-site": "none",
# "sec-fetch-user": "?1",
# "upgrade-insecure-requests": "1",
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
# }

preParse = []
postParse = []

for shop in data["shops"]:

    preParsePcParts = {
        "shopname": shop["shopName"],
        "products": []
    }     

    for product in data["products"]:
        spider = PcPartsSpider(
            shop["baseUrl"],
            shop["query"] + product["name"],
            shop["cssSelectors"]                     
        )              
        preParsePcParts["products"].append({
            "searchQuery": product["name"],
            "removeIfNotContains": product["removeIfNotContains"],
            "category": product["category"],
            "items": spider.CreatePcPartsList()
        })

    preParse.append(preParsePcParts)        
      
        

saveJsonToFile("preParsePcParts", json.dumps(preParse))        
# saveJsonToFile("postParsePcParts", json.dumps(postParse))        



