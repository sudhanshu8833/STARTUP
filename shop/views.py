from binance.client import Client
from .helpful_scripts.object import *
from .views_scripts.refer1 import *
from .views_scripts.all_bots1 import *
from .views_scripts.helpful import *
from .views_scripts.additional import *

from shop.helpful_scripts.tradingview_broker import tradingview_to_brkr
from django.shortcuts import render, redirect
from django.contrib import messages


from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User1

from django.conf import settings
import telepot
import json
bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()



client = Client("GBCTCkf6qgDQSZrPJWp513J69pJ2yVC8Fntdos7REMs5kyWn4ICJ2FNKnX9CM7WW","v0gKOvAfruQaXGbk77W1CsIWf9CVR9kL0U2DEyru2pUwAapXrfyfAMGrEZIdSyaN")

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


        elif brokerr == "5paisa":
            paisa_email = request.POST['paisa_email']
            paisa_password = request.POST['paisa_password']
            paisa_DOB = request.POST['paisa_DOB']
            paisa_api_appname = request.POST['paisa_api_appname']
            paisa_api_appsource = request.POST['paisa_api_appsource']
            paisa_api_userid = request.POST['paisa_api_userid']
            paisa_api_password = request.POST['paisa_api_password']
            paisa_api_userkey = request.POST['paisa_api_userkey']
            paisa_api_encryptkey = request.POST['paisa_api_encryptkey']
            myuser = User1.objects.get(username=current_user)

            # make_object_kucoin(kucoinapi,kucoinsecret,password,myuser.username)

            myuser.paisa_email = paisa_email
            myuser.paisa_password = paisa_password
            myuser.paisa_DOB = paisa_DOB
            myuser.paisa_api_appname = paisa_api_appname
            myuser.paisa_api_appsource = paisa_api_appsource
            myuser.paisa_api_userid = paisa_api_userid
            myuser.paisa_api_password = paisa_api_password
            myuser.paisa_api_userkey = paisa_api_userkey
            myuser.paisa_api_encryptkey = paisa_api_encryptkey
            myuser.save()

            messages.success(request, "Successfully Added/Changed 5paisa Keys")
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



def add_telegram(request):
    current_user = request.user
    if request.method == "POST":
        chat_id=request.POST['telegram_chat_id']
        myuser = User1.objects.get(username=current_user)
        myuser.telegram_chat_id=chat_id
        myuser.save()
        messages.success(request, "Successfully Added/Changed Telegram ID")
        return redirect('index')


def query_message(request):
    print("klsdfjlksdjflksdjflksdjflkdsjlfkjsdklfjsdklfjsdklfjsdklfjksdlfjksldj")

    print(request)
    if request.method == "POST":
        print("######################")
        name=request.POST['name']
        msg_subject=request.POST['msg_subject']
        email=request.POST['email']
        
        budget=request.POST['budget']
        message=request.POST['message']
        print("######################")
        print(name,msg_subject,email,budget,message)

        return redirect('index')
    return redirect('index')
    
@csrf_exempt
def tradingview_webhook(request,passphrase):
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        pp = str(passphrase)

        try:
            myuser = User1.objects.get(passphrase=pp)
        except:
            return HttpResponse("Please send a valid Passphrase, following passphrase doesn't belong to anyone")
        tradingview_to_brkr(myuser, received_json_data, info,bot)

        return HttpResponse(received_json_data)

    return HttpResponse("send a valid post request please")
