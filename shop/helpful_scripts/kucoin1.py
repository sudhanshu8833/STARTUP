from django.http import response
from requests import models

from shop.models import tradingview_orders
import time
import requests
import json






def calculate_quantity(recieved_data,price,client):

    if 'R' in recieved_data['Q']:
        quan=(float(recieved_data['Q'][:-1])/(price*76))

    if 'D' in recieved_data['Q']:
        quan=(float(recieved_data['Q'][:-1])/(price))

    elif '%' in recieved_data['Q']:

        p_l = client.fetch_balance()['USDT']['free']
        quan = ((
            ((float(recieved_data['Q'][:-1]))/100) * p_l)/float(price))
    else:
        quan=recieved_data['Q']

    return (quan)

def send_order(recieved_data,client,quan,price,myuser):
    try:
        
        order_type=recieved_data['OT']
        transaction_type=recieved_data['TT']
        symbol=recieved_data['SYM']
        quantity=quan




        if recieved_data['TT']=='MARKET':
            client.create_order(str(symbol.upper()),str(transaction_type.lower()),str(order_type.lower()),float(quantity))



        if recieved_data['TT']=='LIMIT':
            limit_price=price*(1+int(recieved_data['LIMIT']))
            client.create_order(str(symbol.upper()),str(transaction_type.lower()),str(order_type.lower()),float(quantity),float(limit_price))


        if recieved_data['TT']=='LIMIT':
            p = tradingview_orders(broker="KUCOIN",myuser=myuser.username,symbol=symbol, Price_in=limit_price,time_in=time.time(),order_type=order_type,transaction_type="LIMIT",quantity=quantity)
            p.save()

        if recieved_data['TT']=='MARKET':
            p = tradingview_orders(broker="KUCOIN",myuser=myuser.username,symbol=symbol, Price_in=price, time_in=time.time(),order_type=order_type,transaction_type="MARKET",quantity=quantity)
            p.save()
        return response

    except Exception as e:
        print(str(e))
    

def tradingview_to_kucoin(recieved_data,client,myuser):

    price=recieved_data['PRC']
    quan=calculate_quantity(recieved_data,price,client)
    send_order(recieved_data,client, quan,price,myuser)
        
        





