import string
import requests, bs4

Alp = string.ascii_uppercase[:]
URLS = []
STOCKNAME = []
for i in Alp:
    URLS.append("http://www.moneycontrol.com/india/stockpricequote/" + i)

for url in URLS:
    print url
