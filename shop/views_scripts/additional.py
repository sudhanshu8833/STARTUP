
from django.contrib.auth.decorators import login_required
from shop.models import User1, BOT, BOT1, BOT2, BOT3, BOT4, UserOTP, orders, tradingview_orders,User
from django.shortcuts import render, redirect
from django.contrib import messages
from shop.views import *
from django.core.mail import send_mail
from django.http import HttpResponse
from shop.helpful_scripts.object import *
from django.contrib.auth import authenticate,  login, logout



def about(request):
    return render(request, "shop/about.html")


def contact(request):
    if request.method == "POST":
        # print(request.POST)
        # bot.sendMessage(1039725953, str(request.POST['hello']))
        pass
    return render(request, "shop/contact.html")


def error(request):
    return render(request, "shop/error.html")




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
    return render(request, "shop/add_api_credentials.html", params)