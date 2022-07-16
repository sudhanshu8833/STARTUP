from binance.client import Client
from .helpful_scripts.object import *
from .views_scripts.refer1 import *
from .views_scripts.all_bots1 import *
from .views_scripts.helpful import *
from .views_scripts.additional import *

import string
from shop.helpful_scripts.tradingview_broker import tradingview_to_brkr
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User1, BOT, BOT1, BOT2, BOT3, BOT4, UserOTP, orders, tradingview_orders
import random
from django.core.mail import send_mail
from django.conf import settings
import telepot
import pandas as pd
import json

bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()
# from kucoin.client import Market

client = Client("GBCTCkf6qgDQSZrPJWp513J69pJ2yVC8Fntdos7REMs5kyWn4ICJ2FNKnX9CM7WW",
                "v0gKOvAfruQaXGbk77W1CsIWf9CVR9kL0U2DEyru2pUwAapXrfyfAMGrEZIdSyaN")

info = client.futures_exchange_info()
# from kucoin.client import Trade
# client1 = Trade(key='628f9f8a43ddbc0001e243d2', secret='6c138913-3815-486e-bb97-c6c38c164af1', passphrase='@Support123', is_sandbox=False, url='')



@login_required(login_url='/signup')
def key(request):
    current_user = request.user
    if request.method == "POST":
        brokerr = request.POST['broker']
        print("#####################")
        if brokerr == "binance":
            binanceapi = request.POST['api']
            binancesecret = request.POST['secret']

            myuser = User1.objects.get(username=current_user)

            myuser.binance_API_keys = binanceapi
            myuser.binance_Secret_Keys = binancesecret
            myuser.save()

            # make_object_binance(str(binanceapi),str(binancesecret),str(myuser.username))

            messages.success(
                request, "Successfully Added/Changed Binance Keys")
            return redirect('index')

        elif brokerr == "alpaca":
            alpacaapi = request.POST['api']
            alpacasecret = request.POST['secret']
            alpacatype = request.POST['optradio']
            if alpacatype == "paper":
                uri = "https://paper-api.alpaca.markets"

            else:
                uri = "https://app.alpaca.markets"
            myuser = User1.objects.get(username=current_user)

            # make_object_alpaca(alpacaapi,alpacasecret,uri,myuser.username)

            myuser.alpaca_api_keys = alpacaapi
            myuser.alpaca_secret_keys = alpacasecret
            myuser.alpaca_base_url = uri
            myuser.save()
            messages.success(request, "Successfully Added/Changed Alpaca Keys")
            return redirect('index')

        elif brokerr == "angel":
            angelapi = request.POST['api']
            angelid = request.POST['secret']
            angelpassword = request.POST['optradio']

            myuser = User1.objects.get(username=current_user)

            # make_object_alpaca(alpacaapi,alpacasecret,uri,myuser.username)

            myuser.angel_api_keys = angelapi
            myuser.angel_client_id = angelid
            myuser.angel_password = angelpassword
            myuser.save()
            messages.success(request, "Successfully Added/Changed Angel Keys")
            return redirect('index')

        elif brokerr == "kucoin":
            kucoinapi = request.POST['api']
            kucoinsecret = request.POST['secret']
            password = request.POST['password']
            myuser = User1.objects.get(username=current_user)

            # make_object_kucoin(kucoinapi,kucoinsecret,password,myuser.username)

            myuser.kucoin_api_keys = kucoinapi
            myuser.kucoin_secret_keys = kucoinsecret
            myuser.kucoin_password = password
            myuser.save()
            messages.success(request, "Successfully Added/Changed Alpaca Keys")
            return redirect('index')

        messages.success(request, "Successfully Added/Changed Keys")
        return redirect('index')





@csrf_exempt
def tradingview(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        pp = received_json_data['PP']

        try:
            myuser = User1.objects.get(passphrase=pp)
        except:
            return HttpResponse("Please send a valid Passphrase, following passphrase doesn't belong to anyone")
        tradingview_to_brkr(myuser, received_json_data, info)

        return HttpResponse(received_json_data)

    return HttpResponse("send a valid post request please")






