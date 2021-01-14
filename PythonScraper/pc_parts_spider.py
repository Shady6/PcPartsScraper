from spider import Spider

class PcPartsSpider(Spider):
    def __init__(self, baseUrl, urlExtend, cssSelectors, headers={
        'user-agent': 
        'Mozilla/5.0'        
    }):
        super().__init__(baseUrl, urlExtend, headers)

        self.cssSelectors = cssSelectors


    def CreatePcPartsList(self):
        parentContainer = self.soup.select(self.cssSelectors['container'])
        pcParts = []

        # For debug purpose decrease requests        
        maxiterations = 1
        i = 0

        for child in parentContainer:
            # uncomment for debugging
            if i < maxiterations: 
                pcPart = self.GetText({"name": self.cssSelectors["name"], "price": self.cssSelectors["price"]}, child)                               
                pcPart["producentCode"] = self.GetProducentCode(child)
                pcParts.append(pcPart)
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

   