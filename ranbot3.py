import ccxt
import config
import schedule
from random import randint
import time
from config import marketPair
import warnings
warnings.filterwarnings('ignore')

import numpy as np
from datetime import datetime
import time

exchange = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

in_position = False

def prayRNG():
    global in_position
    rnjesus = randint(0,1)
    print("praying to rnjesus")


    quote = exchange.fetch_balance()["ETH"]['free']
    base = exchange.fetch_balance()["USDT"]['free']
    bids = exchange.fetch_bids_asks()['ETH/USDT']['bid']
    asks = exchange.fetch_bids_asks()['ETH/USDT']['ask']

    buyAmount = base / asks #cals the total balance u can buy by dividing the base price to the asking price
    sellAmount = quote #total ETH balance to sell


    print("Balances: ETH",quote,"USDT",base)

    if rnjesus == 0:
        if not in_position:
            print('jesus says buy')
            if base > 13:
                order = exchange.create_market_buy_order(marketPair, buyAmount)
                print(order)
                in_position = True
            else:
                print('already bought')
        else:
            print('already have monies')


    if rnjesus == 1:
        if in_position:
            print('jesus says sell')
            if quote > 0.01:
                order = exchange.create_market_sell_order(marketPair, sellAmount)
                print(order)
                in_position = False
            else:
                print('selling')
        else:
            print('already sold')

schedule.every(69).seconds.do(prayRNG)

while True:
    schedule.run_pending()
    time.sleep(1)

#started with $230 USD
#ended with $180
#rnjesus not with me
