from pyparsing import col
import yfinance as yf
from finta import TA
import numpy as np


df=yf.download("MSFT",interval="5m",period="1mo")


print(df['Close'].to_numpy())

print(np.reshape(df['Close'].to_numpy(),(len(df['Close']),1)))

