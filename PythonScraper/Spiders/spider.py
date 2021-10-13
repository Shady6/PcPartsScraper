import requests
from bs4 import BeautifulSoup as bs
import os.path
import logging
from Utils.url import *
from Utils.file_saver import saveWebPageToFile
import urllib.parse
import asyncio
import aiohttp


class Spider(object):
    __slots__ = ["baseUrl", "urlExtend", "headers", "soup"]

    @classmethod
    async def create(cls, baseUrl, urlExtend, headers={
        'user-agent':
        'Mozilla/5.0'
    }):
        self = Spider()
        self.baseUrl = baseUrl
        self.urlExtend = urlExtend
        self.headers = headers

        content = await self.LoadContentAsync(self.baseUrl + self.urlExtend)
        self.soup = self.CreateSoup(content)
        return self

    async def LoadContentAsync(self, url):
        try:
            url = parseStringToUrl(url)
            print(f"Sending request to {url}")
            async with aiohttp.ClientSession() as session:
                async with session.get(url=url, headers=self.headers) as response:
                    resp = await response.read()
                    return resp
        except Exception as e:
            print(f"Unable to get url {url}, due to {e.__class__}.")
            return ""

    def LoadContent(self, url):
        try:
            url = parseStringToUrl(url)
            # for debug purpose
            print(f"Sending request to {url}")
            response = requests.get(url, headers=self.headers)
            content = response.content
            response.close()

            # for debug purposes
            # saveWebPageToFile(urllib.parse.urlparse(url).netloc.replace(".", ""), str(content))
            return content
        except:
            print(f"Failed connecting to {url}")
            return None

    def CreateSoup(self, content):
        return bs(content, "html5lib")

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
                selectedText[key] = htmlElement.select_one(
                    cssSelectors[key]).get_text()
            except:
                selectedText[key] = ""
                print(f"Couldn't use css selector for {key}")
                print(htmlElement.select_one(cssSelectors[key]))

        return selectedText

    def GetDefaultHtmlElement(self, htmlElement):
        return htmlElement if htmlElement != None else self.soup
