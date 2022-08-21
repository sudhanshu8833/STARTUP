from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
import json
from .backtesting.backtesting_crypto import run_strategy_crypto
from .backtesting.backtesting_stock import run_strategy_stock


def backtest(request):
    # if request.method=="POST":
    #     data=request.POST['data']
    with open("backtest_model/backtesting/strategy.json") as json_file:
        data=json.load(json_file)
        
    if data['instrument']=="CRYPTO":
        backtest=run_strategy_crypto(data)
        backtest.run()

    if data['instrument']=="STOCK":
        backtest=run_strategy_stock(data)
        backtest.run()

