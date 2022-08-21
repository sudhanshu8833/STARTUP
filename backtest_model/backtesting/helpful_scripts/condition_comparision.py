
import yfinance as yf
from .indicator_ import *

def candle(symbol,time_frame,indicator):
    df=yf.download(symbol,period='1mo',interval=time_frame)

    for key,value in indicator.items():
        df[key]=output(df,key,value['inputs'],value['output'])

    return df


def comparision_output(side):

    _locals = locals()

    exec(
        "value="+side,globals(),_locals
    )

    return value

