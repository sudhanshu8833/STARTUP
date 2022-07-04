from django.http import response
from requests import models

from shop.models import tradingview_orders
import time
import requests
import json






def calculate_quantity(recieved_data,price,client):



    if 'D' in recieved_data['Q']:
        quan=int(float(recieved_data['Q'][:-1])/(price))

    elif '%' in recieved_data['Q']:


        p_l = client.get_account().cash
        quan = int((
            ((float(recieved_data['Q'][:-1]))/100) * p_l)/float(price))
    else:
        quan=recieved_data['Q']

    return int(quan)

def send_order(recieved_data,client,quan,price,username):
    try:
        
        order_type=recieved_data['OT']
        symbol=recieved_data['SYM']
        quantity=quan

        ORDERS_URL = "{}/v2/orders".format(username.alpaca_base_url)
        HEADERS = {'APCA-API-KEY-ID': username.alpaca_api_key, 'APCA-API-SECRET-KEY': username.alpaca_secret_key}


        
        if recieved_data['TT']=='MARKET':
            data = {
            "symbol": str(symbol),
            "qty": quan,
            "side": order_type.lower(),
            "type": "market",
            "time_in_force": recieved_data['TIF'],
            "order_class": "simple"
            # "take_profit": {
            # "limit_price": data['close'] * 1.05
            # },
            # "stop_loss": {
            # "stop_price": data['close'] * 0.98,
            # }
            }
            r = requests.post(ORDERS_URL, json=data, headers=HEADERS)


        if recieved_data['TT']=='LIMIT':
            limit_price=price*(1+int(recieved_data['LIMIT']))


            data = {
            "symbol": str(symbol),
            "qty": quan,
            "side": order_type.lower(),
            "type": "limit",
            "time_in_force": recieved_data['TIF'],
            "order_class": "simple",
            "limit_price":str(limit_price)
            # "take_profit": {
            # "limit_price": data['close'] * 1.05
            # },
            # "stop_loss": {
            # "stop_price": data['close'] * 0.98,
            # }
            }
            r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
            response=json.loads(r.content)
                            
        if recieved_data['TT']=='LIMIT':
            p = tradingview_orders(broker="ALPACA",username=username.username,symbol=symbol, price_in=limit_price,time_in=time.time(),order_type=order_type,transaction_type="LIMIT")
            p.save()

        if recieved_data['TT']=='MARKET':
            p = tradingview_orders(broker="ALPACA",username=username.username,symbol=symbol, price_in=price, time_in=time.time(),order_type=order_type,transaction_type="MARKET")
            p.save()
        return response

    except Exception as e:
        print(str(e))
    

def tradingview_to_alpaca(recieved_data,client,username):

    price=recieved_data['PRC']
    quan=calculate_quantity(recieved_data,price,client)
    send_order(recieved_data, quan,price,username)
        
        





