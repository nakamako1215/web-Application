import requests
from bs4 import BeautifulSoup

url = 'https://www.sejuku.net/blog/'
respons = requests.get(url)
respons.encoding = respons.apparent_encoding

bs = BeautifulSoup(respons.text,'html.parser')

for i in bs.select("a"):
    print(i.getText())

