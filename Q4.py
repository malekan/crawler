import requests
from bs4 import BeautifulSoup






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


