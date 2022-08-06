from pyparsing import col
import yfinance as yf
from finta import TA
import numpy as np
# df=yf.download("MSFT",interval="5m",period="1mo")

data=np.random.rand(3)
c1=True
c2=False
c3=True


exec("value=((c1 and c2) and c3)",globals(),_locals)
print(value)

value=np.where((c1 & c2) | c3,True,False)
print(value)