from bs4 import BeautifulSoup
import requests

url = 'https://coinmarketcap.com'

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

coin_name = soup.find_all('p', class_='sc-1eb5slv-0 iJjGCS')

coin_value = soup.find_all('a', class_='cmc-link')

coin_table = soup.find_all('td')

#for i in coin_name:
    #print(i.text)
    
#for i in coin_value:
    #print(i.text)

#for i in coin_table:
    #if soup.find('span'):
        #i.decompose()
    
class_value = 'sc-1eb5slv-0 iJjGCS'
    
for i in coin_table:
    if class_value in coin_table:
        list.append(i)
        

print(list.text)

#print(coin_table)