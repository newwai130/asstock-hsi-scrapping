import requests
from requests_html import HTMLSession
import json

class AsstockWebHandler:

    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
        return
    
    def getHsiData(self, url):

        response = self.session.get(url, headers=self.headers)
        hsiFutureBlock = response.html.find('div#divContentContainer', first=True).find('div#ssMain', first=True)
        
        hsiFutureNameBlock = hsiFutureBlock.find('select.fs_select', first=True).xpath('//option[@selected]' , first=True)
        hsiFutureName = hsiFutureNameBlock.text
        #print("name", hsiFutureName)
        
        hsiFutureTableBlock = hsiFutureBlock.find('table.tblM', first=True)
        hsiFuturePriceBlock = hsiFutureTableBlock.find('td.content_td1', first=True).find('div.font26', first=True)
        hsiFuturePrice = int(hsiFuturePriceBlock.text.replace(",",""))
        #print("hsi future: ", hsiFuturePrice)

        hsiFutureTimeBlock = hsiFutureTableBlock.find('td.content_td1', first=True).find('div.rmk2', first=True).find('span.cls', first=True)
        hsiFutureTime = hsiFutureTimeBlock.text
        #print("time: ", hsiFutureTime)

        hsiFuturePremiumBlock = hsiFutureTableBlock.find('td.content_td3', first=True).find('span.cls', first=True)
        hsiFuturePremium = int(hsiFuturePremiumBlock.text.replace(",",""))
        if(hsiFutureTableBlock.find('td.content_td3', first=True).find('span.neg', first=True)):
            hsiFuturePremium = -hsiFuturePremium
        #print("premium: ", hsiFuturePremium)

        return AsstrockResponse(hsiFutureName, hsiFuturePrice, hsiFutureTime, hsiFuturePremium)

class AsstrockResponse:
    
    def __init__(self, name, price, time, premium):
        self.name = name
        self.price  = price
        self.time = time
        self. premium = premium

    def toJson(self):
        tempDict = {}
        tempDict['name'] = self.name
        tempDict['price'] = self.price
        tempDict['time'] = self.time
        tempDict['premium'] = self.premium
        return json.dumps(tempDict)

