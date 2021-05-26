import requests
from bs4 import BeautifulSoup

page = requests.get("https://crypto.com/price/")

print(page.status_code)

soup = BeautifulSoup(page.content, "html.parser")

soup.find_all("div")

list(soup.children)

print([type(item) for item in list(soup.children)])

html = list(soup.children)[1]

list(html.children)

print([type(item) for item in list(html.children)])

body = list(html.children)[0]
body2 = list(body.children)[2]

print(list(body2))