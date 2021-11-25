from collections import UserDict
from ccxt.binance import binance
import config
import ccxt
import asyncio
from config import quote
from config import base
from config import marketPair
import pandas as pd

exchange = ccxt.binance({
    "apiKey": config.BINANCE_API_KEY,
    "secret": config.BINANCE_SECRET_KEY
})

quote = exchange.fetch_balance()["ETH"]['free']

base = exchange.fetch_balance()["USDT"]['free']

bids = exchange.fetch_bids_asks()['ETH/USDT']['bid']
asks = exchange.fetch_bids_asks()['ETH/USDT']['ask']

