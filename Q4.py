import requests
from bs4 import BeautifulSoup
import sys
import codecs
mainUrl = "http://meghdadit.com/"
urls_to_scrape = []

r = requests.get(mainUrl)

soup = BeautifulSoup(r.text, "html.parser")

for i in soup.select(".w25p"):
    if i.find('a',href=True):
        urls_to_scrape.append(i.find('a',href=True)['href'])


prices = codecs.open('priceList.txt','w',"utf-8")

for j in urls_to_scrape:
    url_to_scrape = j

    r = requests.get(url_to_scrape)

    soup = BeautifulSoup(r.text,"html.parser")

    priceList = []
    nameList = []
    urlList = []

    for i in soup.select(".item-title-text"):
        nameList.append(i.text)
        urlList.append(i['href'])

    for i in soup.select(".item-price"):
        priceList.append(i.text)

    for i in range(0,len(nameList)):
        prices.write(priceList[i]+" http://meghdadit.com"+urlList[i]+u"\n")

prices.close()