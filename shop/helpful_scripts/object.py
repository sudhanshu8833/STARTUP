# %%
import json
from binance.client import Client
import random
import string
import ccxt

from alpaca_trade_api.rest import REST, TimeFrame

def make_object_binance(binance_api_key,binance_secret_key,username):
    try:

        with open("keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
        print(data3)
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        binance=data3['BINANCE']
        client = Client(binance_api_key,
                        binance_secret_key)

        binance[str(username)]=client

        json_object = json.dumps(data3)
        with open("keys.json", "w") as outfile:
            outfile.write(json_object)

    except Exception as e:
        print(str(e))

def make_object_alpaca(alpaca_api_key,alpaca_secret_key,alpaca_base_url,username):
    try:

        with open("keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
            alpaca=data3['ALPACA']
            client = REST(alpaca_api_key, alpaca_secret_key, alpaca_base_url)

            alpaca[str(username)]=client

            json_object = json.dumps(data3)
            with open("keys.json", "w") as outfile:
                outfile.write(json_object)

    except Exception as e:
        print(str(e))


def make_object_kucoin(kucoin_api_key,kucoin_secret_key,kucoin_password,username):
    try:

        with open("keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
            kucoin=data3['KUCOIN']
            client=ccxt.kucoin({"apiKey":str(kucoin_api_key),"secret":str(kucoin_secret_key),"password":str(kucoin_password)})

            kucoin[str(username)]=client

            json_object = json.dumps(data3)
            with open("keys.json", "w") as outfile:
                outfile.write(json_object)

    except Exception as e:
        print(str(e))



def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))