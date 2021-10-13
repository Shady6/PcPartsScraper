from Spiders.pc_parts_spider import PcPartsSpider
import json
from Utils.file_saver import *
from Parsers.data_parser import parsePcPartsData
from Parsers.filter_with_keyword import filterRecordsNotContainingKeyword
from Parsers.producent_codes_list_creator import createProducentCodesList
from Parsers.to_database_parser import *
from Parsers.filter_with_invalid_producent_code import filterRecordsWithInvalidProducentCode
from DatabaseAccess.save_data import saveAll
import asyncio
from scraper import GetScrapedParts


def dataStepsToFile(preParsePcParts):
    postParsePcParts = parsePcPartsData(preParsePcParts)
    # saveJsonToFile("postParsePcParts", json.dumps(postParsePcParts))
    saveJsonToFile("_all_postParsePcParts", json.dumps(postParsePcParts), True)

    pcPartsTrimmed = filterRecordsNotContainingKeyword(postParsePcParts)
    # saveJsonToFile("pcPartsTrimmed", json.dumps(pcPartsTrimmed))

    pcPartsFilteredByProducentCode = filterRecordsWithInvalidProducentCode(
        postParsePcParts)
    # saveJsonToFile("pcPartsFilteredByProducentCode", json.dumps(pcPartsFilteredByProducentCode))

    producentCodesList = createProducentCodesList(postParsePcParts)
    # saveJsonToFile("producentCodes", json.dumps(producentCodesList))

    pcPartsDbFormat = parsePcPartsToDbFormat(pcPartsFilteredByProducentCode)
    # saveJsonToFile("pcPartsDbFormat", json.dumps(pcPartsDbFormat))
    # saveToCsv("pcPartsDbFormat", pcPartsDbFormat)
    saveToCsv("_all_pcPartsDbFormat", pcPartsDbFormat, True)

    producentCodesDbFormat = parseProducentCodesToDbFormat(producentCodesList)
    # saveJsonToFile("producentCodesDbFormat",json.dumps(producentCodesDbFormat))

    print(
        f"Attempting to save data from {preParsePcParts['shopName']} to database.")
    saveAll()


def loadShopsData():
    shopsData = ""

    with open("./ShopsInputData/shops_debug.json") as f:
        shopsData = json.load(f)
    return shopsData


async def main():
    debug = False
    if not debug:
        shopsData = loadShopsData()

        for shop in shopsData["shops"]:
            scrapedPcParts = await GetScrapedParts(shop, shopsData)

            saveJsonToFile("preParsePcParts", json.dumps(scrapedPcParts))
            saveJsonToFile("_all_preParsePcParts",
                           json.dumps(scrapedPcParts), True)
            dataStepsToFile(scrapedPcParts)

    else:
        preParsePcParts = None
        with open("./_json/preParsePcParts.json") as f:
            preParsePcParts = json.load(f)

        dataStepsToFile(preParsePcParts)


try:
    open("./_json/_all_preParsePcParts.json", "w").close()
    open("./_json/_all_postParsePcParts.json", "w").close()
    open("./_csv/_all_pcPartsDbFormat.csv", "w").close()
except:
    print("No _all files founds, they will be created")

asyncio.run(main())
