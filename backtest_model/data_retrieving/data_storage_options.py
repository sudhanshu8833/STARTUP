from smartapi import SmartWebSocket
import math
import yfinance as yf
from finta import TA
import time
import pandas as pd
import json
import datetime
from dateutil import parser
from datetime import datetime
# %%
from smartapi import SmartConnect
obj = SmartConnect(api_key="uWbpZyYm")
data = obj.generateSession("S776051", "Madhya246###")
refreshToken = data['data']['refreshToken']
feedToken = obj.getfeedToken()
userProfile = obj.getProfile(refreshToken)