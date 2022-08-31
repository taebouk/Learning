import typer
import requests

app = typer.Typer() #Module.method(Class instance)


@app.command(short_help="buy coins")
def buy():
    pass


@app.command(short_help="search for coins") #decorator for a function(denoted by @), basically a meta data for function
def search(coin): #function(paramater)
    coin_api = "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies={}"
    r = requests.get(coin_api.format(coin, "usd"))
    coin_price = r.json()[coin]["usd"]
    print(f"The current price of {coin} is {coin_price}") #fstring allows for integration

if __name__ == "__main__": #dundername has two _, if function in python ends in :, -> if dunder name is main module, app()
    app()