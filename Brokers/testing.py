# import requests
# import pyotp
# import json
# import smartapi

# body={
# "clientcode":"B400150",
# "password":"Pankaj@278",
# "totp":pyotp.TOTP("E6A6M7TCCH2FMY5U3A23FUMXKU").now()
# }

# print(body)
# url="https://apiconnect.angelbroking.com/rest/auth/angelbroking/user/v1/loginByPassword"
# response=requests.get(url,params=body)
# print(response.text)

from finta import TA
import yfinance as yf

b_Bands=yf.download("^NSEBANK",period="1d",interval="1m")

print(TA.BBANDS(b_Bands,period=20))
