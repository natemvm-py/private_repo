#Use the BeautifulSoup and requests Python packages to print out a list of all the article titles on the New York Times homepage.

from bs4 import BeautifulSoup
import requests

url = 'https://www.nytimes.com/'
r = requests.get(url).text

soup = BeautifulSoup(r, features='html.parser')

articleNames = soup.find_all('span', class_='balancedHeadline')

for i in articleNames:
    print(i.text)
print(articleNames)