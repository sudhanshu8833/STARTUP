from django.http import response
from requests import models

from shop.models import tradingview_orders
import time
import requests
import json
# import telepot
# bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
# bot.getMe()





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
    print(quan)
    return (quan)

def send_order(recieved_data,client,quan,price,myuser,bot):
    try:
        
        transaction_type=recieved_data['TT']
        order_type=recieved_data['OT']
        symbol=recieved_data['SYM']
        quantity=quan



 
        if recieved_data['OT']=='MARKET':
            print(str(symbol.upper()))
            print(str(order_type.lower()))
            print(str(transaction_type.lower()))
            print(float(quantity))

            client.create_order(str(symbol.upper()),str(order_type.lower()),str(transaction_type.lower()),float(quantity))



        if recieved_data['OT']=='LIMIT':
            
            if transaction_type=='buy':
                limit_price=price*(1+int(recieved_data['LIMIT']))

            if transaction_type=='sell':
                limit_price=price*(1-int(recieved_data['LIMIT']))



            client.create_order(str(symbol.upper()),str(order_type.lower()),str(transaction_type.lower()),float(quantity),float(limit_price))


        if recieved_data['OT']=='LIMIT':
            p = tradingview_orders(broker="KUCOIN",username=myuser.username,symbol=symbol, Price_in=limit_price,time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()

            if myuser.telegram_chat_id!=0:
                bot.sendMessage(int(myuser.telegram_chat_id),f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type} \n-Quantity:{quantity}\n ----------------------------------- ")
            bot.sendMessage(1039725953,f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type}\n -Quantity:{quantity}\n ----------------------------------- ")



        if recieved_data['OT']=='MARKET':
            p = tradingview_orders(broker="KUCOIN",username=myuser.username,symbol=symbol, Price_in=price, time_in=time.time(),order_type=order_type,transaction_type=transaction_type,quantity=quantity)
            p.save()

            if myuser.telegram_chat_id!=0:
                bot.sendMessage(int(myuser.telegram_chat_id),f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {price} \n -Order Type:{order_type} -Quantity:{quantity}\n ----------------------------------- ")
            bot.sendMessage(1039725953,f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {price} \n -Order Type:{order_type} -Quantity:{quantity}\n ----------------------------------- ")


        return response

    except Exception as e:
        if myuser.telegram_chat_id!=0:
            bot.sendMessage(int(myuser.telegram_chat_id),f"some error occured {str(e)}")

            
        bot.sendMessage(1039725953,f"some error occured --{str(e)} for {myuser.username}")


def tradingview_to_kucoin(recieved_data,client,myuser,bot):

    try:
        price=recieved_data['PRC']

    except:
        pass
    quan=calculate_quantity(recieved_data,price,client)
    
    send_order(recieved_data,client, quan,price,myuser,bot)
        
        





