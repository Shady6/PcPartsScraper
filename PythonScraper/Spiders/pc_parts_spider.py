from Spiders.spider import Spider
from bs4 import Tag


class PcPartsSpider(Spider):
    __slots__ = ["cssSelectors"]
    def __init__(self, baseUrl, urlExtend, cssSelectors, headers={
        'user-agent':
            'Mozilla/5.0'
    }):
        super().__init__(baseUrl, urlExtend, headers)

        self.cssSelectors = cssSelectors

    def CreatePcPartsList(self):
        parentContainer = self.soup.select(self.cssSelectors['container'])
        parentContainer = parentContainer[0].contents if len(parentContainer) == 1 else parentContainer

        pcParts = []

        # For debug purpose decrease requests        
        maxiterations = 1
        i = 0

        for child in (c for c in parentContainer if isinstance(c, Tag)):
            # uncomment for debugging
            if i < maxiterations:
                propertiesToSelect = {"name": self.cssSelectors["name"], "price": self.cssSelectors["price"]}
                if "originalShop" in self.cssSelectors:
                    propertiesToSelect["originalShop"] = self.cssSelectors["originalShop"]

                pcPart = self.GetText(propertiesToSelect, child)
                try:
                    pcPart["producentCode"] = self.GetProducentCode(child)
                    pcParts.append(pcPart)
                except:
                    print("Couldn't get producent code")
                i += 1
        return pcParts

    def GetProducentCode(self, htmlElement):
        producentCode = ""

        if self.cssSelectors["linkToProduct"] == None:
            producentCodeDict = self.GetText({"producentCode": self.cssSelectors["producentCode"]}, htmlElement)
            producentCode = producentCodeDict["producentCode"]
        else:
            absoluteUrl = self.GetAbsoluteUrl(self.cssSelectors["linkToProduct"], htmlElement)
            producentCode = self.GetProducentCodeFromSubPage(absoluteUrl)

        return producentCode

    def GetProducentCodeFromSubPage(self, url):
        subSpider = Spider(url, "")
        producentCodeDict = (
            subSpider.GetText({"producentCode": self.cssSelectors["producentCode"]})
        )

        return producentCodeDict["producentCode"]
