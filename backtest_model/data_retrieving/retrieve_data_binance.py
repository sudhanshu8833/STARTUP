# from aem import Query
from binance.client import Client
from binance import ThreadedWebsocketManager
import psycopg2
import datetime
import json
api_key="GBCTCkf6qgDQSZrPJWp513J69pJ2yVC8Fntdos7REMs5kyWn4ICJ2FNKnX9CM7WW"
secret_key="v0gKOvAfruQaXGbk77W1CsIWf9CVR9kL0U2DEyru2pUwAapXrfyfAMGrEZIdSyaN"

  #sudhanshu real api




db_pass = 'sudhanshu'

def main():

    connection = psycopg2.connect(
        user='postgres',
        password=db_pass,
        host="127.0.0.1",
        port="5432",
        database="postgres"
    )

    cursor = connection.cursor()


    with open("sample.json") as file:
        data=json.load(file)

    stream=[]
    for i in range(1000):
        stream.append((data[i]['symbol']).lower()+"@trade")

    print(stream)
    # stream=["ethusdt@trade","btcusdt@trade","ethbtc@trade","bnbbtc@trade","bnbusdt@trade"]

    twm=ThreadedWebsocketManager(api_key=api_key,api_secret=secret_key)
    twm.start()

    def handle_message(msg,cursor=cursor):
        msg=msg["data"]
        print(msg)
        query= "INSERT INTO raw_trade_data (TIME,SYMBOL,PRICE,QUANTITY)" +\
            "VALUES (%s,%s,%s,%s)"

        timestamp = datetime.datetime.fromtimestamp(msg["T"]/1000)
        record_to_insert = (timestamp,msg["s"],msg['p'],msg['q'])
        cursor.execute(query,record_to_insert)
        connection.commit()

    twm.start_multiplex_socket(callback=handle_message,streams=stream)
    twm.join()



    # {'stream': 'btcusdt@trade', 'data': {'e': 'trade', 'E': 1658661250040,
    #  's': 'BTCUSDT', 't': 1514573132, 'p': '22775.95000000', 'q': '0.01693000',
    #   'b': 11839148456, 'a': 11839148640, 'T': 1658661250040, 'm': True, 'M': True}}



