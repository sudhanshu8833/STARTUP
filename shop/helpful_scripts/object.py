# %%
import json
from binance.client import Client


def make_object(binance_api_key,binance_secret_key,username):
    try:
        with open("keys.json") as json_data_file:
            data3 = json.load(json_data_file)  
            binance=data3['BINANCE']
            client = Client(binance_api_key,
                            binance_secret_key)

            binance[str(username)]=client

            json_object = json.dumps(data3)
            with open("keys.json", "w") as outfile:
                outfile.write(json_object)

    except Exception as e:
        print(str(e))

