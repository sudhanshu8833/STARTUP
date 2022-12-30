from django.shortcuts import render
from django.shortcuts import render, redirect
# Create your views here.
import json
from .backtesting.formula_maker_functions import testing
from .backtesting.backtesting_stock import run_strategy_stock


def backtest(request):
    # if request.method=="POST":
    #     data=request.POST['data']
    with open("backtest_model/backtesting/formula_maker_functions/strategy.json") as json_file:
        data=json.load(json_file)
    
    testing.run(data)
    # if data['instrument']=="CRYPTO":
    #     backtest=run_strategy_crypto(data)
    #     backtest.run()

    # if data['instrument']=="STOCK":
    #     backtest=run_strategy_stock(data)
    #     backtest.run()


def testing(request):

    with open("backtest_model/backtesting/formula_maker_functions/strategy.json") as json_file:
        data=json.load(json_file)
    
    testing.run(data)
