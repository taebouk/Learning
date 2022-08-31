"""
print("Hello Python")

app_name: str = "Crypto Tracker" #":" allows you to hint a variable 

bitcoin_value = 23500

bitcoin_qty_owned = 0.01

in_portfolio = True

null_value = None

coin_names = ["bitcoin", "ethereum", "solana"]
#this is a list

endpoint = ("https", "www.coingecko", "80")#this is a tuple

investment = {"coin_name":"bitcoin", "qty_owned": 0.01} #this is a dictionary

number = {1,2,3,4,5,6}
#this is a set

"""
coin_api = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"
#if you do dir(coin_api), you can see all the commands
import requests

r = requests.get(coin_api.format("bitcoin", "usd"))
coin_data = r.json()
