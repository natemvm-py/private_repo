#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html, features='html.parser')

articleNames = soup.find_all('h3', {'class':'css-xxaj7r e1lsht870'})

count = 1

for i in articleNames:
	print(count, i.text)
	count += 1
