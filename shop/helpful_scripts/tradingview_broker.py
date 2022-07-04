from requests import models
from binance.client import Client
from binance.enums import *
from shop.models import tradingview_orders
import time
import json
from .binance1 import *
from .alpaca1 import *
from .kucoin1 import *



def tradingview_to_brkr(myuser,recieved_data,info):

    
    if "BINANCE" in recieved_data['BRK']:

        with open("./helpful_scripts/keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
        client=data3["BINANCE"][str(myuser.username)]
        tradingview_to_binance(recieved_data,client,info,myuser.username)
        
    if "ALPACA" in recieved_data['BRK']:

        with open("./helpful_scripts/keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
        client=data3["ALPACA"][str(myuser.username)]
        tradingview_to_alpaca(recieved_data,client,myuser)


    if "KUCOIN" in recieved_data['BRK']:

        with open("./helpful_scripts/keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
        client=data3["KUCOIN"][str(myuser.username)]
        tradingview_to_kucoin(recieved_data,client,myuser)


