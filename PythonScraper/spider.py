import requests
from bs4 import BeautifulSoup as bs
import os.path
import logging
from file_saver import *
from url import *

class Spider:
    def __init__(self, baseUrl, urlExtend, headers={
        'user-agent': 
        'Mozilla/5.0'        
    }):
        self.baseUrl = baseUrl
        self.urlExtend = urlExtend
        self.headers = headers   

        content = self.LoadContent(self.baseUrl + self.urlExtend)
        self.soup = self.CreateSoup(content)


    def LoadContent(self, url):
        try:                    
            url = parseStringToUrl(url)
            # for debug purpose
            print(f"Sending request to {url}")
            response = requests.get(url, headers=self.headers)
            content = response.content
            response.close()
            return content    
        except:
            print(f"Failed connecting to {url}")
            return None


    def CreateSoup(self, content):
        return bs(content, 'html.parser')  


    def GetAbsoluteUrl(self, cssSelector, htmlElement=None):
        htmlElement = self.GetDefaultHtmlElement(htmlElement)
        href = htmlElement.select_one(cssSelector)["href"]
        
        if isUrlAbsolute(href):            
            return href
        return self.baseUrl + href


    def GetText(self, cssSelectors, htmlElement=None):
        htmlElement = self.GetDefaultHtmlElement(htmlElement)
        selectedText = {}

        for key in cssSelectors:
            try:
                selectedText[key] = htmlElement.select_one(cssSelectors[key]).get_text()
            except:
                selectedText[key] = ""
                print(f"Couldn't use css selector for {key}")                

        return selectedText


    def GetDefaultHtmlElement(self, htmlElement):
        return htmlElement if htmlElement != None else self.soup   

     