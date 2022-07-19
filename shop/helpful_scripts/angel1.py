from django.http import response
from requests import models

from shop.models import tradingview_orders
import time
import json
import telepot
bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()


def calculate_quantity(recieved_data,price,client):

    if 'R' in recieved_data['Q']:
        quan=int(float(recieved_data['Q'][:-1])/(price))

    else:
        quan=recieved_data['Q']

    return int(quan)

def send_order(recieved_data,client,quan,price,username):
    try:
        
        order_type=recieved_data['OT']
        symbol=recieved_data['SYM']
        quantity=quan
        transaction_type=recieved_data["TT"]
        verify=1
        try:
            if recieved_data['OT']=='MARKET':
                orderparams = {
                    "variety": str(recieved_data['VAR']),
                    "tradingsymbol": str(symbol),
                    "symboltoken": str(recieved_data['TKN']),
                    "transactiontype": str(transaction_type),
                    "exchange": str(recieved_data['EXCH']),
                    "ordertype": "MARKET",
                    "producttype": str(recieved_data['PT']),
                    "duration": str(recieved_data['DUR']),
                    "quantity": str(quantity)
                    }

                orderId=client.placeOrder(orderparams)

            if recieved_data['OT']=='LIMIT':
                if transaction_type=='buy':
                    limit_price=price*(1+int(recieved_data['LIMIT']))

                if transaction_type=='sell':
                    limit_price=price*(1-int(recieved_data['LIMIT']))

                orderparams = {
                    "variety": str(recieved_data['VAR']),
                    "tradingsymbol": str(symbol),
                    "symboltoken": str(recieved_data['TKN']),
                    "transactiontype": str(transaction_type),
                    "exchange": str(recieved_data['EXCH']),
                    "ordertype": "LIMIT",
                    "producttype": str(recieved_data['PT']),
                    "price": str(limit_price),
                    "duration": str(recieved_data['DUR']),
                    "quantity": str(quantity)
                    }

                orderId=client.placeOrder(orderparams)
        except Exception as e:
            if username.telegram_chat_id!=0:
                bot.sendMessage(int(username.telegram_chat_id),f"some error occured {str(e)}")

            verify=0
            bot.sendMessage(1039725953,f"some error occured --{str(e)} for {username.username}")




        if recieved_data['OT']=='LIMIT' and verify==1:
            p = tradingview_orders(broker="ANGEL",username=username.username,symbol=symbol, Price_in=limit_price,time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()

            if username.telegram_chat_id!=0:
                bot.sendMessage(int(username.telegram_chat_id),f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type} -Quantity:{quantity}\n ----------------------------------- ")



        if recieved_data['OT']=='MARKET' and verify==1:
            
            p = tradingview_orders(broker="ANGEL",username=username.username,symbol=symbol, Price_in=price, time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()

            if username.telegram_chat_id!=0:
                bot.sendMessage(int(username.telegram_chat_id),f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type} -Quantity:{quantity}\n ----------------------------------- ")



        return response

    except Exception as e:
        print(str(e))
    

def tradingview_to_angel(recieved_data,client,username):

    price=recieved_data['PRC']
    quan=calculate_quantity(recieved_data,price,client)
    send_order(recieved_data,client, quan,price,username)
        
        





