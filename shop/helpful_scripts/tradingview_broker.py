from requests import models
from binance.client import Client
from binance.enums import *
from shop.models import tradingview_orders
import time
import json
from .binance1 import *
from .alpaca1 import *
from .kucoin1 import *
from .angel1 import *
from .fivepaisa1 import *
from .paper1 import *
import traceback
from alpaca_trade_api.rest import REST, TimeFrame
import ccxt
from smartapi import SmartConnect 
from py5paisa.order import Order, OrderType, AHPlaced
from py5paisa import FivePaisaClient


def tradingview_to_brkr(myuser,recieved_data,info,bot):
    try:
        if "BINANCE" in recieved_data['BRK']:

            client=Client(myuser.binance_API_keys,myuser.binance_Secret_Keys)
            tradingview_to_binance(recieved_data,client,info,myuser,bot)
            
        if "ALPACA" in recieved_data['BRK']:

            client = REST(myuser.alpaca_api_keys, myuser.alpaca_secret_keys, myuser.alpaca_base_url)
            tradingview_to_alpaca(recieved_data,client,myuser,bot)

        if "KUCOIN" in recieved_data['BRK']:
            print(str(myuser.kucoin_api_keys))
            print(str(myuser.kucoin_secret_keys))
            print(str(myuser.kucoin_password))


            client=ccxt.kucoin({"apiKey":str(myuser.kucoin_api_keys),"secret":str(myuser.kucoin_secret_keys),"password":str(myuser.kucoin_password)})
            print("#######################")
            tradingview_to_kucoin(recieved_data,client,myuser,bot)

        if "ANGEL" in recieved_data['BRK']:
            
            client=SmartConnect(api_key=str(myuser.angel_api_keys))
            data = client.generateSession(str(myuser.angel_client_id),str(myuser.angel_password))
            tradingview_to_angel(recieved_data,client,myuser,bot)


        if "PAPER" in recieved_data['BRK']:
            tradingview_to_paper(recieved_data,myuser,bot)



        if "5PAISA" in recieved_data['BRK']:
            config={
                "APP_NAME":str(myuser.paisa_api_appname),
                "APP_SOURCE":str(myuser.paisa_api_appsource),
                "USER_ID":str(myuser.paisa_api_userid),
                "PASSWORD":str(myuser.paisa_api_password),
                "USER_KEY":str(myuser.paisa_api_userkey),
                "ENCRYPTION_KEY":str(myuser.paisa_api_encryptkey)
                }

            client = FivePaisaClient(email=str(myuser.paisa_email), passwd=str(myuser.paisa_password), dob=str(myuser.paisa_DOB),cred=config)
            client.login()

            tradingview_to_5paisa(recieved_data,client,myuser,bot)

    except Exception as e:
        bot.sendMessage(1039725953,str(traceback.format_exc()))


