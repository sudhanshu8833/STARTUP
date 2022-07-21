from django.shortcuts import render, redirect
from shop.models import User1, BOT, BOT, BOT1, BOT2, BOT3, BOT4
from django.contrib import messages
import datetime
from shop.views import *
from django.contrib.auth.decorators import login_required
from .refer1 import *

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
    