from sqlalchemy import null
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
from .models import User1, BOT, BOT1, BOT2, BOT3, BOT4, UserOTP, orders, tradingview_orders
from django.contrib.auth.decorators import login_required

import random
from django.core.mail import send_mail
from django.conf import settings
import telepot
import pandas as pd
import json
bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()
import string
from .helpful_scripts.object import *
# from kucoin.client import Market

from binance.client import Client
client = Client("GBCTCkf6qgDQSZrPJWp513J69pJ2yVC8Fntdos7REMs5kyWn4ICJ2FNKnX9CM7WW",
                "v0gKOvAfruQaXGbk77W1CsIWf9CVR9kL0U2DEyru2pUwAapXrfyfAMGrEZIdSyaN")

info = client.futures_exchange_info()
# from kucoin.client import Trade
# client1 = Trade(key='628f9f8a43ddbc0001e243d2', secret='6c138913-3815-486e-bb97-c6c38c164af1', passphrase='@Support123', is_sandbox=False, url='')
###################################################

@login_required(login_url='/signup')
def refer(request, bot_price):

    person_a = 20
    person_b = 20
    person_c = 15
    person_d = 10
    person_e = 5
    print(bot_price)
    print("****************************")
    current_user = request.user
    actual_user = User1.objects.get(username=current_user)
    refer_1 = actual_user.another_referral

    if refer_1 == 'NONE':
        return redirect('index')

    refer_1_object = User1.objects.get(username=refer_1)
    refer_1_object.credit += person_a*bot_price/100
    refer_1_object.save()


    refer_2 = refer_1_object.another_referral

    if refer_2 == 'NONE':
        return redirect('index')
    refer_2_object = User1.objects.get(username=refer_2)
    refer_2_object.credit += person_b*bot_price/100
    refer_2_object.save()



    refer_3 = refer_2_object.another_referral

    if refer_3 == 'NONE':
        return redirect('index')
    refer_3_object = User1.objects.get(username=refer_3)
    refer_3_object.credit += person_c*bot_price/100
    refer_3_object.save()

    refer_4 = refer_3_object.another_referral


    if refer_4 == 'NONE':
        return redirect('index')
    refer_4_object = User1.objects.get(username=refer_4)
    refer_4_object.credit += person_d*bot_price/100
    refer_4_object.save()




    refer_5 = refer_4_object.another_referral

    if refer_5 == 'NONE':
        return redirect('index')
    refer_5_object = User1.objects.get(username=refer_5)
    refer_5_object.credit += person_e*bot_price/100
    refer_5_object.save()

    return redirect('index')

###################################################

@login_required(login_url='/signup')
def key(request):
    current_user = request.user
    if request.method == "POST":
        brokerr=request.POST['broker']
        print("#####################")
        if brokerr=="binance":
            binanceapi = request.POST['api']
            binancesecret = request.POST['secret']
            
            myuser = User1.objects.get(username=current_user)

            

            myuser.binance_API_keys = binanceapi
            myuser.binance_Secret_Keys = binancesecret
            myuser.save()


            # make_object_binance(str(binanceapi),str(binancesecret),str(myuser.username))



            messages.success(request, "Successfully Added/Changed Binance Keys")
            return redirect('index')

        elif brokerr=="alpaca":
            alpacaapi = request.POST['api']
            alpacasecret = request.POST['secret']
            alpacatype=request.POST['optradio']
            if alpacatype=="paper":
                uri="https://paper-api.alpaca.markets"

            else:
                uri="https://app.alpaca.markets"
            myuser = User1.objects.get(username=current_user)

            # make_object_alpaca(alpacaapi,alpacasecret,uri,myuser.username)

            myuser.alpaca_api_keys = alpacaapi
            myuser.alpaca_secret_keys = alpacasecret
            myuser.alpaca_base_url=uri
            myuser.save()
            messages.success(request, "Successfully Added/Changed Alpaca Keys")
            return redirect('index')

        elif brokerr=="kucoin":
            kucoinapi = request.POST['api']
            kucoinsecret = request.POST['secret']
            password=request.POST['password']
            myuser = User1.objects.get(username=current_user)

            # make_object_kucoin(kucoinapi,kucoinsecret,password,myuser.username)

            myuser.kucoin_api_keys = kucoinapi
            myuser.kucoin_secret_keys = kucoinsecret
            myuser.kucoin_password=password
            myuser.save()
            messages.success(request, "Successfully Added/Changed Alpaca Keys")
            return redirect('index')


        messages.success(request, "Successfully Added/Changed Keys")
        return redirect('index')


def terms(request):

    return render(request, "shop/terms.html")




@csrf_exempt
def tradingview(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        pp=received_json_data['PP']
        # print(received_json_data)
        try:
            myuser = User1.objects.get(passphrase=pp)
        except:
            return HttpResponse("Please send a valid Passphrase, following passphrase doesn't belong to anyone")
        tradingview_to_brkr(myuser,received_json_data,info)
        

        return HttpResponse(received_json_data)


    return HttpResponse("send a valid post request please")
        # if received_json_data['BRK']=="BINANCE":
            

        #     order_type=received_json_data['OT']
        #     symbol=received_json_data['SYM']
        #     quantity=received_json_data['Q']
            
            # bot.sendMessage(1039725953, str(received_json_data))
            # 


def home(request):
    return render(request, "shop/home1.html")





def contact(request):
    if request.method == "POST":
        # print(request.POST)
        # bot.sendMessage(1039725953, str(request.POST['hello']))
        pass
    return render(request, "shop/contact.html")




def error(request):
    return render(request, "shop/error.html")


@login_required(login_url='/signup')
def all_bots(request):
    current_user = request.user
    actual_user = User1.objects.get(username=current_user)
    if request.method == "POST":
        buy_item = request.POST['buy_item']
        obj = BOT.objects.get(title=buy_item)
        if(buy_item == 'BOT1'):
            if (actual_user.credit > obj.Price):
                today = datetime.datetime.now()
                buy = BOT1(binance_API_keys=actual_user.binance_API_keys, binance_Secret_Keys=actual_user.binance_Secret_Keys,
                           Expiry_date=today, email=current_user.email, Max_loss=0)
                buy.save()
                actual_user.credit -= obj.Price
                actual_user.security += obj.price/6
                actual_user.save()
                messages.success(
                    request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
                refer(request, obj.Price)
                return redirect('index')

            else:
                messages.error(
                    request, f"Unfortunately, you don't have enough money to purchase {obj.title}!")
                return redirect('index')
        if(buy_item == 'BOT2'):
            if (actual_user.credit > obj.Price):
                today = datetime.datetime.now()
                buy = BOT2(binance_API_keys=actual_user.binance_API_keys, binance_Secret_Keys=actual_user.binance_Secret_Keys,
                           Expiry_date=today, email=current_user.email, Max_loss=0)

                buy.save()
                actual_user.credit -= obj.Price
                actual_user.security += obj.price/6
                actual_user.save()
                messages.success(
                    request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
                refer(request, obj.Price)
                return redirect('index')
            else:
                messages.error(
                    request, f"Unfortunately, you don't have enough money to purchase {obj.title}!")
                return redirect('index')

        if(buy_item == 'BOT3'):
            if (actual_user.credit > obj.Price):
                today = datetime.datetime.now()
                buy = BOT3(angel_API_keys=actual_user.angel_API_keys, username=actual_user.angel_username,
                           password=actual_user.angel_password, Expiry_date=today, email=current_user.email, Max_loss=0)
                buy.save()
                actual_user.credit -= obj.Price
                actual_user.security += obj.price/6
                actual_user.save()
                messages.success(
                    request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
                refer(request, obj.Price)
                return redirect('index')
            else:
                messages.error(
                    request, f"Unfortunately, you don't have enough money to purchase {obj.title}!")
                return redirect('index')
        if(buy_item == 'BOT4'):
            if (actual_user.credit > obj.Price):
                today = datetime.datetime.now()
                buy = BOT4(angel_API_keys=actual_user.angel_API_keys, username=actual_user.angel_username,
                           password=actual_user.angel_password, Expiry_date=today, email=current_user.email, Max_loss=0)
                buy.save()
                actual_user.credit -= obj.Price
                actual_user.security += obj.price/6
                actual_user.save()
                messages.success(
                    request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
                refer(request, obj.Price)
                return redirect('index')
            else:
                messages.error(
                    request, f"Unfortunately, you don't have enough money to purchase {obj.title}!")
                return redirect('index')

    total = []
    total2 = []
    buy1 = None
    try:
        buy1 = BOT1.objects.get(email=current_user.email)
    except:
        pass
    if(buy1 is None):

        Buy1 = BOT.objects.get(bot_id=1)
        text = Buy1.description
        main = text.split("\ ")
        total2.append(main)

        actual_user = User1.objects.get(username=current_user)
        if actual_user.free == 1:
            Buy1.Price = 0

        total.append(Buy1)
    buy2 = None
    try:
        buy2 = BOT2.objects.get(email=current_user.email)
    except:
        pass
    if(buy2 is None):
        Buy2 = BOT.objects.get(bot_id=2)
        text = Buy2.description
        main = text.split("\ ")
        total2.append(main)
        total.append(Buy2)
    buy3 = None
    try:
        buy3 = BOT3.objects.get(email=current_user.email)
    except:
        pass
    if(buy3 is None):
        Buy3 = BOT.objects.get(bot_id=3)
        text = Buy3.description
        main = text.split("\ ")
        total2.append(main)
        total.append(Buy3)
    buy4 = None
    try:
        buy4 = BOT4.objects.get(email=current_user.email)
    except:
        pass
    if(buy4 is None):
        Buy4 = BOT.objects.get(bot_id=4)
        text = Buy4.description
        main = text.split("\ ")
        total2.append(main)
        total.append(Buy4)
    zipped = zip(total, total2)

    myuser = User1.objects.get(username=current_user)
    params = {'zipped': zipped, 'myuser': myuser}
    return render(request, "shop/all_bots.html", params)

@login_required(login_url='/signup')
def user_bots(request):
    current_user = request.user
    if request.method == "POST":
        buy_item = request.POST['buy_item']
        maxloss = request.POST['maxloss']
        if(buy_item == 'BOT1'):
            a = BOT1.objects.get(email=current_user.email)
            a.Max_loss = maxloss
            a.save()
            messages.success(
                request, f"Maximum Loss is successfully stored for {buy_item} ")
            return redirect("index")
        if(buy_item == 'BOT2'):
            a = BOT2.objects.get(email=current_user.email)
            a.Max_loss = maxloss
            a.save()
            messages.success(
                request, f"Maximum Loss is successfully stored for {buy_item} ")
            return redirect("index")
        if(buy_item == 'BOT3'):
            a = BOT3.objects.get(email=current_user.email)
            a.Max_loss = maxloss
            a.save()
            messages.success(
                request, f"Maximum Loss is successfully stored for {buy_item} ")
            return redirect("index")
        if(buy_item == 'BOT4'):
            a = BOT4.objects.get(email=current_user.email)
            a.Max_loss = maxloss
            a.save()
            messages.success(
                request, f"Maximum Loss is successfully stored for {buy_item} ")
            return redirect("index")
    total = []
    total2 = []
    buy1 = None
    try:
        buy1 = BOT1.objects.get(email=current_user.email)
    except:
        pass
    if(buy1):
        Buy1 = BOT.objects.get(title="BOT1")
        total.append(Buy1)
        total2.append(buy1)
    buy2 = None
    try:
        buy2 = BOT2.objects.get(email=current_user.email)
    except:
        pass
    if(buy2):
        Buy2 = BOT.objects.get(title="BOT2")
        total.append(Buy2)
        total2.append(buy2)
    buy3 = None
    try:
        buy3 = BOT3.objects.get(email=current_user.email)
    except:
        pass
    if(buy3):
        Buy3 = BOT.objects.get(title="BOT3")
        total.append(Buy3)
        total2.append(buy3)
    buy4 = None
    try:
        buy4 = BOT4.objects.get(email=current_user.email)
    except:
        pass
    if(buy4):
        Buy4 = BOT.objects.get(title="BOT4")
        total.append(Buy4)
        total2.append(buy4)
    zipped = zip(total, total2)
    params = {'zipped': zipped}
    return render(request, "shop/user_bots.html", params)

@login_required(login_url='/signup')
def add_api(request):
    current_user = request.user
    myuser = User1.objects.get(username=current_user)
    params = {'myuser': myuser}
    return render(request, "shop/add_api_credentials.html",params)


@login_required(login_url='/signup')
def setting(request):
    current_user = request.user
    if request.method == "POST":
        fullname = request.POST['fullname']
        number = request.POST['number']
        ifsc = request.POST['ifsc']
        binanceapi = request.POST['binanceapi']
        binancesecret = request.POST['binancesecret']
        angelapi = request.POST['angelapi']
        angelusername = request.POST['angelusername']
        angelpassword = request.POST['angelpassword']
        myuser = User1.objects.get(username=current_user)
        myuser.fullname = fullname
        myuser.ifsc = ifsc
        myuser.account_num = number
        myuser.binance_API_keys = binanceapi
        myuser.binance_Secret_Keys = binancesecret
        myuser.angel_API_keys = angelapi
        myuser.angel_username = angelusername
        myuser.angel_password = angelpassword
        myuser.save()
        buy1 = None
        try:
            buy1 = BOT1.objects.get(email=current_user.email)
        except:
            pass
        if(buy1):
            buy1.binance_API_keys = binanceapi
            buy1.binance_Secret_Keys = binancesecret
            buy1.save()
        buy2 = None
        try:
            buy2 = BOT2.objects.get(email=current_user.email)
        except:
            pass
        if(buy2):
            buy2.binance_API_keys = binanceapi
            buy2.binance_Secret_Keys = binancesecret
            buy2.save()
        buy3 = None
        try:
            buy3 = BOT3.objects.get(email=current_user.email)
        except:
            pass
        if(buy3):
            buy3.angel_API_keys = angelapi
            buy3.angel_username = angelusername
            buy3.angel_password = angelpassword
        buy4 = None
        try:
            buy4 = BOT4.objects.get(email=current_user.email)
        except:
            pass
        if(buy4):
            buy4.angel_API_keys = angelapi
            buy4.angel_username = angelusername
            buy4.angel_password = angelpassword
        messages.success(request, "Your details added successfully!!")
        return redirect('index')
    myuser = User1.objects.get(username=current_user)
    params = {'myuser': myuser}
    return render(request, "shop/settings.html", params)

@login_required(login_url='/signup')
def checkout(request):
    return render(request, "shop/checkout.html")


@login_required(login_url='/signup')
def bots(request):
    current_user = request.user
    total = []
    total2 = []
    Buy1 = BOT.objects.get(bot_id=1)
    text = Buy1.description
    main = text.split("\ ")
    total2.append(main)
    total.append(Buy1)
    Buy2 = BOT.objects.get(bot_id=2)
    text = Buy2.description
    main = text.split("\ ")
    total2.append(main)
    total.append(Buy2)
    Buy3 = BOT.objects.get(bot_id=3)
    text = Buy3.description
    main = text.split("\ ")
    total2.append(main)
    total.append(Buy3)
    Buy4 = BOT.objects.get(bot_id=4)
    text = Buy4.description
    main = text.split("\ ")
    total2.append(main)
    total.append(Buy4)
    zipped = zip(total, total2)
    myuser = User1.objects.get(username=current_user)
    params = {'zipped': zipped, 'myuser': myuser}
    return render(request, "shop/bot_details.html", params)


def signup(request):
    if request.method=="GET":
        myuser=request.user
        print(type(myuser))
        # if myuser.is_anonymous():
        #     print("##################")
    if request.method == "POST":
        get_otp = request.POST.get('otp')
        if get_otp:
            get_user = request.POST.get('usr')
            usr = User.objects.get(username=get_user)
            usr2 = User1.objects.get(username=get_user)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                usr2.is_active = True
                usr2.save()
                messages.success(
                    request, " Your Account has been successfully created")
                login(request, usr)
                return redirect('index')
            else:
                messages.warning(request, " You Entered wrong OTP !")
                return redirect(request, "shop/login.html", {'otp': True, 'usr': usr})
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['pass1']
        confpassword = request.POST['pass2']
        if len(username) > 10:
            messages.error(
                request, " Your user name must be under 10 characters")
            return redirect('signup')
        if not username.isalnum():
            messages.error(
                request, " User name should only contain letters and numbers")
            return redirect('signup')
        if (password != confpassword):
            messages.error(request, " Passwords do not match")
            return redirect('signup')

        match = None
        try:
            match = User1.objects.get(email=email)
        except User1.DoesNotExist:
            pass
        if(match):
            messages.error(request, " This email is already registered !! ")
            return redirect('signup')
        match = None
        try:
            match = User1.objects.get(phone=phone)
        except User1.DoesNotExist:
            pass
        if(match):
            messages.error(
                request, " This Phone Number is already registered !! ")
            return redirect('signup')
        match = None
        try:
            match = User1.objects.get(username=username)
        except User1.DoesNotExist:
            pass
        if(match):
            messages.error(request, " This username is already registered !! ")
            return redirect('signup')
        myuser = User.objects.create_user(username, email, password)
        myuser.is_active = False
        myuser.save()

        chars = string.ascii_letters
        size = 20

        user = User1(username=username, 
                        email=email,
                         password=password, 
                         phone=phone,
                        fullname='XYZ', 
                        binance_API_keys='NONE', 
                        binance_Secret_Keys='NONE'
                        ,alpaca_api_keys="NONE",
                        alpaca_secret_keys="NONE",
                        alpaca_base_url="https://app.alpaca.markets"
                     , passphrase=random_string_generator(size, chars))

        user.save()
        usr_otp = random.randint(100000, 999999)
        UserOTP.objects.create(user=myuser, otp=usr_otp)
        mess = f"Hello {username} \n\nYour OTP is {usr_otp} \n\n, Please Do not share it with anyone..!!\n If you didn't requested to login, you can safely ignore this email..!!\n\n You may be required to register with the Site. You agree to keep your password confidential and will be responsible for all use of your account and password. We reserve the right to remove, reclaim, or change a username you select if we determine, in our sole discretion, that such username is inappropriate, obscene, or otherwise objectionable. \n\nAlgo99\n H.no. 381, Rajendra Nagar, Pathakhera, Distt- Betul \nBetul, Madhya Pradesh 460449 \nIndia \nPhone: 9145814438 \nalgo99.sudhanshu@gmail.com"
        send_mail(
            "Welcome to algo99 -Verify Your Email",
            mess,
            settings.EMAIL_HOST_USER,
            [myuser.email],
            fail_silently=False
        )
        messages.success(request,"OTP is sent to your email..!!!")
        return render(request, "shop/login.html", {'otp': True, 'usr': myuser})
    return render(request, "shop/login.html")

@login_required(login_url='/signup')
def index(request):
    current_user = request.user
    total = []
    # total2 = []
    Buy1 = tradingview_orders.objects.all().filter(username=current_user)
    for i in Buy1:
        total.append(i)
    # print(buy1)
    # params={'zipped':zipped}
    myuser = User1.objects.get(username=current_user)
    print(total)
    params = {'myuser': myuser, 'total': total}
    return render(request, "shop/index.html", params)


def handleLogin(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == "POST":
        print(request.user)
        get_otp = request.POST.get('otp')

        if get_otp:
            get_user = request.POST.get('usr')
            usr = User.objects.get(username=get_user)
            usr2 = User1.objects.get(username=get_user)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                usr2.is_active = True
                usr2.save()
                login(request, usr)
                # messages.success(request, "Successfully Logged In")
                return redirect("index")
            else:
                messages.warning(request, " You Entered wrong OTP !")
                return redirect(request, "shop/login.html", {'otp': True, 'usr': usr})
        loginusername = request.POST['username']
        loginpassword = request.POST['password']
        user = authenticate(username=loginusername, password=loginpassword)
        if user is not None:
            myuser = User1.objects.get(username=loginusername)
            params = {'myuser': myuser}
            # messages.success(request, "Successfully Logged In")
            login(request, user)
            # return redirect('index',params)
            return redirect("index")
        elif not User.objects.filter(username=loginusername).exists():
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("signup")
        elif not User.objects.get(username=loginusername).is_active:
            myuser = User.objects.get(username=loginusername)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=myuser, otp=usr_otp)
            mess = f"Hello {loginusername} \n\nYour OTP is {usr_otp} \n\n, Please Do not share it with anyone..!!\n If you didn't requested to login, you can safely ignore this email..!!\n\n You may be required to register with the Site. You agree to keep your password confidential and will be responsible for all use of your account and password. We reserve the right to remove, reclaim, or change a username you select if we determine, in our sole discretion, that such username is inappropriate, obscene, or otherwise objectionable. \n\nAlgo99\n H.no. 381, Rajendra Nagar, Pathakhera, Distt- Betul \nBetul, Madhya Pradesh 460449 \nIndia \nPhone: 9145814438 \nalgo99.sudhanshu@gmail.com"
            send_mail(
                "Welcome to algo99 -Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [myuser.email],
                fail_silently=False
            )
            messages.success(request,"OTP is sent to your email..!!!")
            return render(request, "shop/login.html", {'otp': True, 'usr': myuser})
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("signup")

    return HttpResponse("404- Not found")


def handleLogout(request):
    logout(request)
    return redirect('/')


def withdraw(request):

    print("withdrawn amount")
    messages.success(
        request, "Request Sent Succesfully, Your money will be withdrawn in 3 working days")
    return redirect('index')


def resendOTP(request):
    if request.method == "GET":
        get_usr = request.GET['usr']
        if User.objects.filter(username=get_usr).exists() and not User.objects.get(username=get_usr).is_active:
            usr = User.objects.get(username=get_usr)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            mess = f"Hello {get_usr} \n\nYour OTP is {usr_otp} \n\n, Please Do not share it with anyone..!!\n If you didn't requested to login, you can safely ignore this email..!!\n\n You may be required to register with the Site. You agree to keep your password confidential and will be responsible for all use of your account and password. We reserve the right to remove, reclaim, or change a username you select if we determine, in our sole discretion, that such username is inappropriate, obscene, or otherwise objectionable. \n\nAlgo99\n H.no. 381, Rajendra Nagar, Pathakhera, Distt- Betul \nBetul, Madhya Pradesh 460449 \nIndia \nPhone: 9145814438 \nalgo99.sudhanshu@gmail.com"
            send_mail(
                "Welcome to algo99 -Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            messages.success(request,"OTP is sent to your email..!!!")
            return HttpResponse("Resend")
    return HttpResponse("Can't Send")
