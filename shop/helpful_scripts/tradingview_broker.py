from requests import models
from binance.client import Client
from binance.enums import *
from shop.models import tradingview_orders
import time
import json
from .binance1 import *
from .alpaca1 import *
from .kucoin1 import *
from alpaca_trade_api.rest import REST, TimeFrame
import ccxt

def tradingview_to_brkr(myuser,recieved_data,info):

    if "BINANCE" in recieved_data['BRK']:

        client=Client(myuser.binance_API_keys,myuser.binance_Secret_Keys)
        tradingview_to_binance(recieved_data,client,info,myuser.username)
        
    if "ALPACA" in recieved_data['BRK']:

        client = REST(myuser.alpaca_api_keys, myuser.alpaca_secret_keys, myuser.alpaca_base_url)
        tradingview_to_alpaca(recieved_data,client,myuser)

    if "KUCOIN" in recieved_data['BRK']:
        
        client=ccxt.kucoin({"apiKey":str(myuser.kucoin_api_keys),"secret":str(myuser.kucoin_secret_keys),"password":str(myuser.kucoin_password)})
        tradingview_to_kucoin(recieved_data,client,myuser)


