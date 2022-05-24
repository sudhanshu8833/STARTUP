from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate,  login, logout
from django.contrib.auth.models import User
import datetime
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from django.http import HttpResponse
from .models import User1, BOT, BOT1, BOT2, BOT3, BOT4, UserOTP
import random
from django.core.mail import send_mail
from django.conf import settings
import telepot
import pandas as pd
import json
bot = telepot.Bot('5365452349:AAElPqo1y-SHXCVcf7EqGCdZ80P858ouiW0')
bot.getMe()


###################################################
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

# 55555555555555555
    refer_2 = refer_1_object.another_referral

    if refer_2 == 'NONE':
        return redirect('index')
    refer_2_object = User1.objects.get(username=refer_2)
    refer_2_object.credit += person_b*bot_price/100
    refer_2_object.save()


#    nnnnnn
    refer_3 = refer_2_object.another_referral

    if refer_3 == 'NONE':
        return redirect('index')
    refer_3_object = User1.objects.get(username=refer_3)
    refer_3_object.credit += person_c*bot_price/100
    refer_3_object.save()

    refer_4 = refer_3_object.another_referral
# nnnnnnnnnnnnnn

    if refer_4 == 'NONE':
        return redirect('index')
    refer_4_object = User1.objects.get(username=refer_4)
    refer_4_object.credit += person_d*bot_price/100
    refer_4_object.save()


# mnmmmmmmmmmmmm

    refer_5 = refer_4_object.another_referral

    if refer_5 == 'NONE':
        return redirect('index')
    refer_5_object = User1.objects.get(username=refer_5)
    refer_5_object.credit += person_e*bot_price/100
    refer_5_object.save()

    return redirect('index')

###################################################


def key(request):
    current_user = request.user
    if request.method == "POST":
        binanceapi = request.POST['api']
        binancesecret = request.POST['secret']
        myuser = User1.objects.get(username=current_user)
        myuser.binance_API_keys = binanceapi
        myuser.binance_Secret_Keys = binancesecret
        myuser.save()
        messages.success(request, "Successfully Added/Changed Keys")
        return redirect('index')


def home(request):
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


    
    params = {'zipped': zipped}
    return render(request, "shop/home1.html", params)


def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        # print(request.POST)
        # bot.sendMessage(1039725953, str(request.POST['hello']))
        pass
    return render(request, "shop/contact.html")


@csrf_exempt
def tradingview(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        print(received_json_data)
        bot.sendMessage(1039725953, str(received_json_data))
        return HttpResponse(received_json_data)



def error(request):
    return render(request, "shop/error.html")


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


def checkout(request):
    return render(request, "shop/checkout.html")


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
                return redirect('all_bots')
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
        user = User1(username=username, email=email, password=password, phone=phone,
                     fullname='XYZ', binance_API_keys='NONE', binance_Secret_Keys='NONE')
        user.save()
        usr_otp = random.randint(100000, 999999)
        UserOTP.objects.create(user=myuser, otp=usr_otp)
        mess = f"Hello {username} \nYour OTP is {usr_otp}\nThanks!!"
        send_mail(
            "Welcome to algo99 -Verify Your Email",
            mess,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False
        )
        return render(request, "shop/login.html", {'otp': True, 'usr': myuser})
    return render(request, "shop/login.html")


def index(request):
    current_user = request.user
    total = []
    total2 = []
    buy1 = None
    try:
        buy1 = BOT1.objects.get(email=current_user.email)
    except:
        pass
    if(buy1):
        Buy1 = BOT.objects.get(bot_id=1)
        total.append(Buy1)
        total2.append(buy1)
    buy2 = None
    try:
        buy2 = BOT2.objects.get(email=current_user.email)
    except:
        pass
    if(buy2):
        Buy2 = BOT.objects.get(bot_id=1)
        total.append(Buy2)
        total2.append(buy2)
    buy3 = None
    try:
        buy3 = BOT3.objects.get(email=current_user.email)
    except:
        pass
    if(buy3):
        Buy3 = BOT.objects.get(bot_id=1)
        total.append(Buy3)
        total2.append(buy3)
    buy4 = None
    try:
        buy4 = BOT4.objects.get(email=current_user.email)
    except:
        pass
    if(buy4):
        Buy4 = BOT.objects.get(bot_id=1)
        total.append(Buy4)
        total2.append(buy4)
    zipped = zip(total, total2)
    # params={'zipped':zipped}
    myuser = User1.objects.get(username=current_user)
    params = {'myuser': myuser, 'zipped': zipped}
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
                messages.success(request, "Successfully Logged In")
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
            messages.success(request, "Successfully Logged In")
            login(request, user)
            # return redirect('index',params)
            return redirect("all_bots")
        elif not User.objects.filter(username=loginusername).exists():
            messages.error(request, "Invalid credentials! Please try again")
            return redirect("signup")
        elif not User.objects.get(username=loginusername).is_active:
            myuser = User.objects.get(username=loginusername)
            usr_otp = random.randint(100000, 999999)
            UserOTP.objects.create(user=myuser, otp=usr_otp)
            mess = f"Hello {loginusername} \nYour OTP is {usr_otp}\nThanks!!"
            send_mail(
                "Welcome to algo99 -Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [myuser.email],
                fail_silently=False
            )
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
            mess = f"Hello {get_usr} \nYour OTP is {usr_otp}\nThanks!!"
            send_mail(
                "Welcome to algo99 -Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return HttpResponse("Resend")
    return HttpResponse("Can't Send")
