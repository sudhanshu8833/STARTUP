from django.http import response
from requests import models

from shop.models import tradingview_orders
import time
import json
import telepot
bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()


def calculate_quantity(recieved_data, price, client):

    if 'R' in recieved_data['Q']:
        quan = int(float(recieved_data['Q'][:-1])/(price))
    else:
        quan = recieved_data['Q']

    return int(quan)


def send_order(recieved_data, client, quan, price, username):
    try:

        order_type = recieved_data['OT']

        if recieved_data['TT'] == 'buy':
            order_type = 'B'
        elif recieved_data['TT'] == 'sell':
            order_type = 'S'

        if recieved_data['EXCH'] == 'NSE':
            exchange = "N"
        if recieved_data['EXCH'] == 'BSE':
            exchange = "B"
        if recieved_data['EXCH'] == 'MCX':
            exchange = "M"

        if recieved_data['DUR'] == 'DAY':
            duration = 0
        if recieved_data['DUR'] == 'EOS':
            duration = 4
        if recieved_data['DUR'] == 'GTC':
            duration = 2
        if recieved_data['DUR'] == 'GTD':
            duration = 1
        if recieved_data['DUR'] == 'IOC':
            duration = 3
        if recieved_data['DUR'] == 'FOK':
            duration = 6

        if recieved_data['PT'] == 'CASH':
            product = 'C'
        if recieved_data['PT'] == 'DERIVATIVE':
            product = 'D'
        if recieved_data['PT'] == 'CURRENCY':
            product = 'U'

        symbol = recieved_data['SYM']
        quantity = quan
        transaction_type = recieved_data["TT"]

        if recieved_data['OT'] == 'MARKET':

            response = client.place_order(OrderType=order_type, Exchange=exchange, ExchangeType=product, ScripCode=int(
                recieved_data['TKN']), Qty=quan, Price=0, iOrderValidity=duration)

        if recieved_data['OT'] == 'LIMIT':
            if transaction_type == 'buy':
                limit_price = price*(1+int(recieved_data['LIMIT']))

            if transaction_type == 'sell':
                limit_price = price*(1-int(recieved_data['LIMIT']))

            response = client.place_order(OrderType=order_type, Exchange=exchange, ExchangeType=product, ScripCode=int(
                recieved_data['TKN']), Qty=quan, Price=limit_price, iOrderValidity=duration)

        if recieved_data['OT'] == 'LIMIT':
            p = tradingview_orders(broker="5PAISA", username=username.username, symbol=symbol, Price_in=limit_price, time_in=time.time(
            ), order_type=order_type, transaction_type=transaction_type, quantity=quantity)
            p.save()

            if username.telegram_chat_id != 0:
                bot.sendMessage(int(username.telegram_chat_id),
                                f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type}\n -Quantity:{quantity}\n ----------------------------------- ")

        if recieved_data['OT'] == 'MARKET':
            p = tradingview_orders(broker="5PAISA", username=username.username, symbol=symbol, Price_in=price, time_in=time.time(
            ), order_type=order_type, transaction_type=transaction_type, quantity=quantity)
            p.save()

            if username.telegram_chat_id != 0:
                bot.sendMessage(int(username.telegram_chat_id),
                                f"-Time open: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))} \n -Symbol: {symbol} \n -Side: {transaction_type} \n - Price: {limit_price} \n -Order Type:{order_type}\n -Quantity:{quantity}\n ----------------------------------- ")

        return response

    except Exception as e:
        if username.telegram_chat_id != 0:
            bot.sendMessage(int(username.telegram_chat_id),
                            f"some error occured {str(e)}")

        bot.sendMessage(
            1039725953, f"some error occured --{str(e)} for {username.username}")


def tradingview_to_5paisa(recieved_data, client, username):

    price = recieved_data['PRC']
    quan = calculate_quantity(recieved_data, price, client)
    send_order(recieved_data, client, quan, price, username)
