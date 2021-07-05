import requests

url = 'https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=100&sortBy=market_cap&sortType=desc&convert=USD,BTC,ETH&cryptoType=all&tagType=all&audited=false&aux=ath,atl,high24h,low24h,num_market_pairs,cmc_rank,date_added,tags,platform,max_supply,circulating_supply,total_supply,volume_7d,volume_30d'
response = requests.get(url)

data = response.json()

final_list = []
temp = []
for each_crypto in data['data']['cryptoCurrencyList']:
    temp.append(each_crypto['name'])

    # each_crypto['quotes'] gives you list of price and market gap of each crypto
    for quote in each_crypto['quotes']:
        # assuming you want to get USD price of each crypto
        if quote['name'] == "USD":
            temp.append(quote['price'])
            temp.append(quote['marketCap'])

    final_list.append(temp)
    temp = []
    
print(temp)
print(final_list)