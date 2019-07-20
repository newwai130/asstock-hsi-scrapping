import requests
from requests_html import HTMLSession

class EnetWebHandler():

    def __init__(self):
        self.session = HTMLSession()
        self.headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'}
        return
    
    def getHsiData(self, url):
        response = self.session.get(url, headers=self.headers)
        hsiFutureBlock = response.html.find('div.FuturesQuoteContent', first=True)
        hsiFuturePriceBlock = hsiFutureBlock.find('div.FuturesQuoteNominal', first=True)
        hsiFuturePrice = int(hsiFuturePriceBlock.text.replace(",",""))
        
        hsiFuturePricePremiumBlock = hsiFutureBlock.find('div.FuturesQuotePremium', first=True)
        tempHsiFuturePricePremiumString = hsiFuturePricePremiumBlock.text.replace("高水","+").replace("低水","-")
        hsiFuturePricePremium = int(tempHsiFuturePricePremiumString)

        print(hsiFuturePricePremium)

