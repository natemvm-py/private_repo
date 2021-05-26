import requests
from bs4 import BeautifulSoup

url = "http://help.websiteos.com/websiteos/example_of_a_simple_html_page.htm"


res = requests.get(url)

soup = BeautifulSoup(res.text, "html.parser")

print(type(soup))

whs2 = soup.find_all("p", {"class": "whs2"})

title = whs2[2].getText()

print(title)