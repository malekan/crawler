import requests
from bs4 import BeautifulSoup

mainUrl = "http://meghdadit.com/"
urls_to_scrape = []

r = requests.get(mainUrl)

soup = BeautifulSoup(r.text, "html.parser")

for i in soup.select(".w25p"):
    if i.find('a',href=True):
        urls_to_scrape.append(i.find('a',href=True)['href'])

for i in urls_to_scrape:
    print(i)


url_to_scrape = 'http://meghdadit.com/productlist/20/b.19/ipp.40/'

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


