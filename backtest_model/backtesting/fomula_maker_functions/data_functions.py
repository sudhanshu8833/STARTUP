import yfinance as yf
import numpy as np

def numpy_comversion(series):
    return np.reshape(series.to_numpy(),(len(series),1))

def ltp_price(symbol,period,interval):
    ltp_price=algo_get_data(symbol, period, interval)['Close']
    return numpy_comversion(ltp_price)


def algo_get_data(symbol, period, interval):
    data = yf.download(symbol, period=period, interval=interval)
    return data


def algo_get_close(symbol, period, interval):
    data = algo_get_data(symbol, period, interval)
    data_close = data['Close']
    return numpy_comversion(data_close)


def algo_get_open(symbol, period, interval):
    data = algo_get_data(symbol, period, interval)
    data_open = data['Open']
    return numpy_comversion(data_open)


def algo_get_high(symbol, period, interval):
    data = algo_get_data(symbol, period, interval)
    data_high = data['High']
    return numpy_comversion(data_high)


def algo_get_low(symbol, period, interval):
    data = algo_get_data(symbol, period, interval)
    data_low = data['Low']
    return numpy_comversion(data_low)


def algo_get_volume(symbol, period, interval):
    data = algo_get_data(symbol, period, interval)
    data_volume = data['Volume']
    return numpy_comversion(data_volume)


def algo_get_adj_close(symbol, period, interval):
    data = algo_get_data(symbol, period, interval)
    data_adj_close = data['Adj Close']
    return numpy_comversion(data_adj_close)

