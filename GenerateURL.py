import string
import requests, bs4

Alp = string.ascii_uppercase[:]
URLS = []
STOCKNAME = []
for i in Alp:
    URLS.append("http://www.moneycontrol.com/india/stockpricequote/" + i)


for url in URLS:
    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    for sname in soup.find_all("a",{"class" : "bl_12"}):
        STOCKNAME.append(sname.get("title"))



print len(STOCKNAME)

for stock in STOCKNAME:
    print stock
