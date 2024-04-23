from flask import Flask, render_template
from pycoingecko import CoinGeckoAPI

app = Flask(__name__)
cg = CoinGeckoAPI()

def btc_data():
    # get data bitcoin vs usd in last 100 days
    data = cg.get_coin_market_chart_by_id('bitcoin', 'usd', '100days')
    # unix timestamp
    dates = [rec[0] for rec in data['prices']]
    # price in usd
    prices = [rec[1] for rec in data['prices']]
    return dates, prices

@app.route("/")
def main():
    dates, prices = btc_data()
    return render_template("index.html", dates=dates, prices=prices)