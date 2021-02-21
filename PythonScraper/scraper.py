from Spiders.pc_parts_spider import PcPartsSpider
import asyncio


async def GetScrapedParts(shop, shopsData):
    scrapedPcParts = {
        "shopName": shop["shopName"],
        "currency": shop["currency"],
        "products": []
    }

    spiders = await asyncio.gather(*[CreatePcSpider(shop, product)
            for product
            in shopsData["products"]
            if IsCategoryIncluded(shop, product)])
    pcPartsList = await gather_with_concurrency(1, *[spider.CreatePcPartsList()
            for spider, product
            in zip(spiders, shopsData["products"])
            if IsCategoryIncluded(shop, product)])
    scrapedPcParts["products"] = CreateProducts(shopsData, pcPartsList)

    return scrapedPcParts

async def gather_with_concurrency(n, *tasks):
    semaphore = asyncio.Semaphore(n)

    async def sem_task(task):
        async with semaphore:
            return await task
    return await asyncio.gather(*(sem_task(task) for task in tasks))

async def CreateSpiders(shop, shopsData):
    return [await CreatePcSpider(shop, product)
            for product
            in shopsData["products"]
            if IsCategoryIncluded(shop, product)]


async def CreatePcPartsList(shop, shopsData, spiders):
    return [await spider.CreatePcPartsList()
            for spider, product
            in zip(spiders, shopsData["products"])
            if IsCategoryIncluded(shop, product)]


def CreateProducts(shopsData, pcPartsList):
    return [CreateProductWithItems(product, pcParts)
            for product, pcParts
            in zip(shopsData["products"], pcPartsList)]


async def CreatePcSpider(shop, product):
    return await PcPartsSpider.create(shop["baseUrl"],
                                (shop["queryPrefix"][product[
                                    "category"]] if "queryPrefix" in shop else "") +
                                shop["query"] + product["name"],
                                shop["cssSelectors"])


def IsCategoryIncluded(shop, product):
    return "excludeCategories" not in shop or product["category"] not in shop[
        "excludeCategories"]


def CreateProductWithItems(product, pcParts):
    return {
        "searchQuery": product["name"],
        "mustInclude": product["mustInclude"],
        "category": product["category"],
        "items": pcParts
    }


# old synchronous implementation (sloow)

# for product in shopsData["products"]:
#     if "excludeCategories" not in shop or product["category"] not in shop["excludeCategories"]:
#         print(f"Searching in: {shop['shopName']}, for: {product['name']}")
#         try:
#             queryPrefix = shop["queryPrefix"][product["category"]] if "queryPrefix" in shop else ""
#             spider = PcPartsSpider(
#                 shop["baseUrl"],
#                 queryPrefix + shop["query"] + product["name"],
#                 shop["cssSelectors"]
#             )
#             scrapedPcParts["products"].append({
#                 "searchQuery": product["name"],
#                 "mustInclude": product["mustInclude"],
#                 "category": product["category"],
#                 "items": spider.CreatePcPartsList()
#             })
#         except:
#             print(f"Couldn't connect with {shop['shopName']}, url: { shop['baseUrl'] + queryPrefix + shop['query'] + product['name']}")
