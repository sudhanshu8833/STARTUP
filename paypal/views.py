from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from shop.models import User1,BOT,BOT1,BOT2,BOT3,BOT4
import datetime
from django.http import JsonResponse
import json
idd=0

def payments(request):
    return render(request,"paypal/payments.html")
def payment_1(request):
    if request.method=="POST":
        titlee=request.POST['amount']
        bots=BOT.objects.get(title=titlee)
        amount=bots.Price
        idd=bots.bot_id
        print(amount)
    return  render(request, 'paypal/paypal.html', {'amount': amount})

def processOrder(request):
    data=json.loads(request.body)
    total=float(data['form']['total'])
    current_user=request.user
    actual_user=User1.objects.get(username=current_user)
    obj=BOT.objects.get(bot_id=idd)
    if(obj.bot_id==1):
        today=datetime.datetime.now()
        buy=BOT1(binance_API_keys=actual_user.binance_API_keys,binance_Secret_Keys=actual_user.binance_Secret_Keys,Expiry_date=today,email=current_user.email,Max_loss=0)
        buy.save()
        messages.success(request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
        return redirect('index')
    if(obj.bot_id==2):
        today=datetime.datetime.now()
        buy=BOT2(binance_API_keys=actual_user.binance_API_keys,binance_Secret_Keys=actual_user.binance_Secret_Keys,Expiry_date=today,email=current_user.email,Max_loss=0)
        buy.save()
        messages.success(request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
        return redirect('index')
    if(obj.bot_id==3):
        today=datetime.datetime.now()
        buy=BOT3(angel_API_keys=actual_user.angel_API_keys,username=actual_user.angel_username,password=actual_user.angel_password,Expiry_date=today,email=current_user.email,Max_loss=0)
        buy.save()
        messages.success(request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
        return redirect('index')
    if(obj.bot_id==4):
        today=datetime.datetime.now()
        buy=BOT4(angel_API_keys=actual_user.angel_API_keys,username=actual_user.angel_username,password=actual_user.angel_password,Expiry_date=today,email=current_user.email,Max_loss=0)
        buy.save()
        messages.success(request, f"Congratulations! You purchased {obj.title} for Rs {obj.Price}")
        return redirect('index')
    messages.success(request, f"Payment Successful, credits has been added...!")
    return redirect('index')
