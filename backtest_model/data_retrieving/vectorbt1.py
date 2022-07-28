
import vectorbt as vbt
import numpy as np
from binance.client import Client
import pandas as pd
import datetime as dt
import json
import requests

client = Client("GBCTCkf6qgDQSZrPJWp513J69pJ2yVC8Fntdos7REMs5kyWn4ICJ2FNKnX9CM7WW","v0gKOvAfruQaXGbk77W1CsIWf9CVR9kL0U2DEyru2pUwAapXrfyfAMGrEZIdSyaN")


def candle(symbol, interval):


    root_url = 'https://api.binance.com/api/v1/klines'
    url = root_url + '?symbol=' + symbol + '&interval=' + interval
    data = json.loads(requests.get(url).text)
    df = pd.DataFrame(data)
    df.columns = ['Datetime',
                'Open', 'High', 'Low', 'Close', 'volume',
                'close_time', 'qav', 'num_trades',
                'taker_base_vol', 'taker_quote_vol', 'ignore']
    df.index = [dt.datetime.fromtimestamp(x / 1000.0) for x in df.close_time]
    
    df.drop(['close_time','qav','num_trades','taker_base_vol', 'taker_quote_vol', 'ignore'],axis=1,inplace=True)
           
    
    df['Open']=pd.to_numeric(df["Open"], downcast="float")
    df["High"]=pd.to_numeric(df["High"], downcast="float")
    df["Low"]=pd.to_numeric(df["Low"], downcast="float")
    df["Close"]=pd.to_numeric(df["Close"], downcast="float")
    df["volume"]=pd.to_numeric(df["volume"], downcast="float")
    # print(df)
    return df

df=candle("BTCUSDT",'5m')

btc_price=df['Close']

# rsi=vbt.RSI.run(btc_price,window=10)

def custom_indicator(close,rsi_window=14,ma_window=50):
    rsi=vbt.RSI.run(close,window=rsi_window).rsi.to_numpy()
    ma=vbt.MA.run(close,ma_window).ma.to_numpy()

    trend=np.where(rsi>70,-1,0)
    trend=np.where((rsi<30)&(close<ma),1,trend)
    return trend



ind=vbt.IndicatorFactory(
    class_name="combination",
    short_name="comb",
    input_names=["close"],
    param_names=["rsi_window","ma_window"],
    output_names=["value"]

).from_apply_func(
    custom_indicator,
    rsi_window=14,
    ma_window=50
)


res=ind.run(
    btc_price,
    rsi_window=[21,20,19,10]
)

entries=res.value==1.0
exits=res.value==-1.0

pf=vbt.Portfolio.from_signals(btc_price,entries,exits)

print(entries)
print(exits)
# print(entries.to_string())


print(pf.stats())
