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
        
        transaction_type=recieved_data['TT']
        order_type=recieved_data['OT']
        symbol=recieved_data['SYM']
        quantity=quan




        if recieved_data['OT']=='MARKET':
            client.create_order(str(symbol.upper()),str(order_type.lower()),str(transaction_type.lower()),float(quantity))



        if recieved_data['OT']=='LIMIT':
            
            if transaction_type=='buy':
                limit_price=price*(1+int(recieved_data['LIMIT']))

            if transaction_type=='sell':
                limit_price=price*(1-int(recieved_data['LIMIT']))

            client.create_order(str(symbol.upper()),str(order_type.lower()),str(transaction_type.lower()),float(quantity),float(limit_price))


        if recieved_data['OT']=='LIMIT':
            p = tradingview_orders(broker="KUCOIN",myuser=myuser.username,symbol=symbol, Price_in=limit_price,time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()

        if recieved_data['OT']=='MARKET':
            p = tradingview_orders(broker="KUCOIN",myuser=myuser.username,symbol=symbol, Price_in=price, time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()
        return response

    except Exception as e:
        print(str(e))
    

def tradingview_to_kucoin(recieved_data,client,myuser):

    price=recieved_data['PRC']
    quan=calculate_quantity(recieved_data,price,client)
    send_order(recieved_data,client, quan,price,myuser)
        
        





