from Spiders.spider import Spider
from bs4 import Tag
import asyncio


class PcPartsSpider(Spider):
    __slots__ = ["cssSelectors", "super"]

    @classmethod
    async def create(cls, baseUrl, urlExtend, cssSelectors, headers={
        'user-agent':
            'Mozilla/5.0'
    }):
        self = PcPartsSpider()
        self.super = await super().create(baseUrl, urlExtend, headers)

        self.cssSelectors = cssSelectors
        return self

    async def CreatePcPartsList(self):
        parentContainer = self.super.soup.select(self.cssSelectors['container'])
        parentContainer = parentContainer[0].contents if len(parentContainer) == 1 else parentContainer

        # pcParts = []

        # For debug purpose decrease requests        
        maxiterations = 1
        i = 0

        htmlTags = [child for child in parentContainer if isinstance(child, Tag)]
        pcParts = await asyncio.gather(*[self.GetPcPart(child) for child in htmlTags])

        # for child in (c for c in parentContainer if isinstance(c, Tag)):
        #     # uncomment for debugging
        #     # if i < maxiterations:
        #
        #     i += 1
        return pcParts

    async def GetPcPart(self, htmlElement):
        propertiesToSelect = {"name": self.cssSelectors["name"], "price": self.cssSelectors["price"]}
        if "originalShop" in self.cssSelectors:
            propertiesToSelect["originalShop"] = self.cssSelectors["originalShop"]

        pcPart = self.super.GetText(propertiesToSelect, htmlElement)
        try:
            pcPart["producentCode"] = await self.GetProducentCode(htmlElement)
        except:
            print("Couldn't get producent code")
            pcPart["producentCode"] = ""
        return pcPart


    async def GetProducentCode(self, htmlElement):
        producentCode = ""

        if self.cssSelectors["linkToProduct"] == None:
            producentCodeDict = self.GetText({"producentCode": self.cssSelectors["producentCode"]}, htmlElement)
            producentCode = producentCodeDict["producentCode"]
        else:
            absoluteUrl = self.super.GetAbsoluteUrl(self.cssSelectors["linkToProduct"], htmlElement)
            producentCode = await self.GetProducentCodeFromSubPage(absoluteUrl)

        return producentCode

    async def GetProducentCodeFromSubPage(self, url):
        subSpider = await Spider.create(url, "")
        # subSpider = Spider(url, "")
        producentCodeDict = (
            subSpider.GetText({"producentCode": self.cssSelectors["producentCode"]})
        )

        return producentCodeDict["producentCode"]
