from requests import models
from binance.client import Client
from binance.enums import *
from shop.models import tradingview_orders
import time


def ltp_price(instrument,client):
    prices = client.get_all_tickers()
    for i in range(len(prices)):
        if prices[i]['symbol'] == str(instrument):

            return float(prices[i]['price'])

def get_precision(symbol,info):

    for x in info['symbols']:
        if x['symbol'] == symbol:
            return x['quantityPrecision']

def calculate_quantity(recieved_data,price,info,client):

    if 'R' in recieved_data['Q']:
        precision=get_precision(recieved_data['SYM'],info)
        quan=round(float(recieved_data['Q'][:-1])/(price*76),int(precision))

    elif 'D' in recieved_data['Q']:
        precision=get_precision(recieved_data['SYM'],info)
        quan=round(float(recieved_data['Q'][:-1])/(price),int(precision))

    elif '%' in recieved_data['Q']:
        data = client.futures_account_balance()
        for i in range(len(data)):
            if data[i]['asset'] == 'USDT':
                p_l = float(data[i]['withdrawAvailable'])
        quan = (
            ((float(recieved_data['Q'][:-1]))/100) * p_l)/float(price)
    else:
        quan=recieved_data['Q']

    return quan

def send_order(recieved_data,client,quan,price,info,username):
    try:
        precision=get_precision(recieved_data['SYM'],info)
        transaction_type=recieved_data['TT']
        symbol=recieved_data['SYM']
        quantity=round(quan,precision)
        if recieved_data['OT']=='MARKET':
            if transaction_type=="BUY":
                order1 = client.futures_create_order(
                            symbol=str(symbol),
                            side="BUY",
                            type="MARKET",

                            quantity=quantity)

            if transaction_type=="SELL":
                order1 = client.futures_create_order(
                            symbol=str(symbol),
                            side="SELL",
                            type="MARKET",

                            quantity=quantity)



        if recieved_data['OT']=='LIMIT':
            limit_price=price*(1+int(recieved_data['LIMIT']))
            


            if transaction_type=="BUY":
                order1 = client.futures_create_order(
                            symbol=str(symbol),
                            side="BUY",
                            type="LIMIT",
                            timeInForce=recieved_data["TIF"],
                            quantity=quantity,
                            price=limit_price)


            if transaction_type=="SELL":
                order1 = client.futures_create_order(
                            symbol=str(symbol),
                            side="SELL",
                            type="LIMIT",
                            timeInForce=recieved_data["TIF"],
                            quantity=quantity,
                            price=limit_price)
                            
        if recieved_data['OT']=='LIMIT':
            p = tradingview_orders(broker="BINANCE",username=username,symbol=symbol, Price_in=limit_price,time_in=time.time(),transaction_type=transaction_type,order_type="LIMIT",quantity=quantity)
            p.save()

        if recieved_data['OT']=='MARKET':
            p = tradingview_orders(broker="BINANCE",username=username,symbol=symbol, Price_in=price, time_in=time.time(),transaction_type=transaction_type,order_type="MARKET",quantity=quantity)
            p.save()
        return order1
    except Exception as e:
        print(str(e))


def tradingview_to_binance(recieved_data,client,info,username):

    price=ltp_price(recieved_data['SYM'],client)
    quan=calculate_quantity(recieved_data,price,info,client)
    send_order(recieved_data, client, quan,price,info,username)
        
        





