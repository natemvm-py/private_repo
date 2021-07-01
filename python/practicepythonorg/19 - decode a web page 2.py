#Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
#The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.
#(Hint: The post here describes in detail how to use the BeautifulSoup and requests libraries through the solution of the exercise posted here.)
#This will just print the full text of the article to the screen. It will not make it easy to read, so next exercise we will learn how to write this text to a .txt file.

from bs4 import BeautifulSoup
import requests

url = 'https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture'
r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser')

articleHeading = soup.find('h1', class_='content-header__row content-header__hed')
articleSubHeading = soup.find('div', class_='content-header__row content-header__dek')
articleText = soup.select('p')

print(articleHeading.text)
print(articleSubHeading.text)
for i in articleText:
    print(i.text)