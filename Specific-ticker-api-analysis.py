#install "requests" using pip install requests
#install "JSON" using pip install json
#this api displays ticker data for a specific cryptocurrency.
# Use the "id" field from the Listings endpoint in the URL.

import requests #importing libraries
import json #importing libraries

convert = 'USD' #the currency fromat we intend to have

listing_url = 'https://api.coinmarketcap.com/v2/listings/' #the api link
url_end = '?structure=array&convert=' + convert # here we append the currency to the link

request = requests.get(listing_url) #getting the data and converting it into json
results = request.json()

data = results['data']

ticker_url_pairs = {} #empty dictionary
for currency in data:
    symbol = currency['symbol']
    url = currency['id']
    ticker_url_pairs[symbol] = url #storing as a key value pair.

print(ticker_url_pairs) #id and symbol pairs

while True:

    print()
    choice = input("Enter the ticker symbol of a cryptocurrency: ") #ask for the currency
    choice = choice.upper() #uppercasing the input

    ticker_url = 'https://api.coinmarketcap.com/v2/ticker/' + str(ticker_url_pairs[choice]) + '/' + url_end
    #appending to the url

    request = requests.get(ticker_url)
    results = request.json()

    print(json.dumps(results, sort_keys=True, indent=4)) #printing the data

    currency = results['data'][0] #storing the data attribute into currency for zeroth index only
                                  #since there is only one index in it

    rank = currency['rank']
    name = currency['name']
    symbol = currency['symbol']

    circulating_supply = int(currency['circulating_supply']) #typecasting
    total_supply = int(currency['total_supply'])

    quotes = currency['quotes'][convert] #storing the data
    market_cap = quotes['market_cap']
    hour_change = quotes['percent_change_1h']
    day_change = quotes['percent_change_24h']
    week_change = quotes['percent_change_7d']
    price = quotes['price']
    volume = quotes['volume_24h']

    volume_string = '{:,}'.format(volume) #formating to strings
    market_cap_string = '{:,}'.format(market_cap)
    circulating_supply_string = '{:,}'.format(circulating_supply)
    total_supply_string = '{:,}'.format(total_supply)

    print(str(rank) + ': ' + name + ' (' + symbol + ')') #printing the outputs
    print('Market cap: \t\t$' + market_cap_string)
    print('Price: \t\t\t$' + str(price))
    print('24h Volume: \t\t$' + volume_string)
    print('Hour change: \t\t' + str(hour_change) + '%')
    print('Day change: \t\t' + str(day_change) + '%')
    print('Week change: \t\t' + str(week_change) + '%')
    print('Total supply: \t\t' + total_supply_string)
    print('Circulating supply: \t' + circulating_supply_string)
    print('Percentage of coins in circulation: ' + str(int(circulating_supply / total_supply * 100)))
    print()

    choice = input('Again? (y/n): ') #asking the user for choice

    if choice == 'n': #if no then break from the loop
        break
