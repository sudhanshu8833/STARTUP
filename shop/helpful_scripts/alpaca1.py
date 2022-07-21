from django.http import response
from requests import models

from shop.models import tradingview_orders
import time
import requests
import json


import telepot
bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()



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
        transaction_type=recieved_data["TT"]
        ORDERS_URL = "{}/v2/orders".format(username.alpaca_base_url)
        HEADERS = {'APCA-API-KEY-ID': username.alpaca_api_keys, 'APCA-API-SECRET-KEY': username.alpaca_secret_keys}
        verify=1
        try:
            if recieved_data['OT']=='MARKET':
                data = {
                "symbol": str(symbol),
                "qty": quan,
                "side": transaction_type.lower(),
                "type": "market",
                "time_in_force": recieved_data['TIF'].lower(),
                "order_class": "simple"
                # "take_profit": {
                # "limit_price": data['close'] * 1.05
                # },
                # "stop_loss": {
                # "stop_price": data['close'] * 0.98,
                # }
                }
                r = requests.post(ORDERS_URL, json=data, headers=HEADERS)
                response=json.loads(r.content)
                

            if recieved_data['OT']=='LIMIT':
                if transaction_type=='buy':
                    limit_price=price*(1+int(recieved_data['LIMIT']))

                if transaction_type=='sell':
                    limit_price=price*(1-int(recieved_data['LIMIT']))


                data = {
                "symbol": str(symbol),
                "qty": quan,
                "side": transaction_type.lower(),
                "type": "limit",
                "time_in_force": recieved_data['TIF'].lower(),
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
            
        except Exception as e:
            if username.telegram_chat_id!=0:
                bot.sendMessage(int(username.telegram_chat_id),f"some error occured {str(e)}")

            verify=0
            bot.sendMessage(1039725953,f"some error occured {str(e)} for {username.username}")


        if recieved_data['OT']=='LIMIT' and verify==1:
            p = tradingview_orders(broker="ALPACA",username=username.username,symbol=symbol, Price_in=limit_price,time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()
            if username.telegram_chat_id!=0:
                bot.sendMessage(int(username.telegram_chat_id),f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type}\n -Quantity:{quantity}\n ----------------------------------- ")



        if recieved_data['OT']=='MARKET' and verify==1:
            p = tradingview_orders(broker="ALPACA",username=username.username,symbol=symbol, Price_in=price, time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()

            if username.telegram_chat_id!=0:
                bot.sendMessage(int(username.telegram_chat_id),f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {price} \n -Order Type:{order_type}\n -Quantity:{quantity}\n ----------------------------------- ")

        return response

    except Exception as e:
        print(str(e))
    

def tradingview_to_alpaca(recieved_data,client,username):

    price=recieved_data['PRC']
    quan=calculate_quantity(recieved_data,price,client)
    send_order(recieved_data,client, quan,price,username)
        
        





