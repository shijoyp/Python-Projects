import requests, bs4

res = requests.get('http://www.moneycontrol.com/india/stockpricequote/A')

soup = bs4.BeautifulSoup(res.text, "html.parser")

for sname in soup.find_all("a",{"class" : "bl_12"}):
    print(sname.get("title"))


