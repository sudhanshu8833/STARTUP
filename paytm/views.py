from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages 
from django.views.decorators.csrf import csrf_exempt
from paytm import checksum
from shop.models import User1,BOT,BOT4,BOT3,BOT1,BOT2
import time,datetime
MERCHANT_KEY='x&Iog9XRoBP6r6hB'
idd=0


def payments(request):
    return render(request,"paytm/payments.html")



def payment_1(request):
    if request.method=="POST":
        titlee=request.POST['amount']
        bots=BOT.objects.get(title=titlee)
        if bots.bot_id==1:
            current_user=request.user
            actual_user=User1.objects.get(username=current_user)
            if actual_user.free == 1:
                today=datetime.datetime.now()
                buy=BOT1(binance_API_keys=actual_user.binance_API_keys,binance_Secret_Keys=actual_user.binance_Secret_Keys,Expiry_date=today,email=current_user.email,Max_loss=0)
                buy.save()
                actual_user.free=2
                actual_user.save()
                messages.success(request, f"Congratulations! Free trial Started ")
                return redirect('index')
        amount=bots.Price
        idd=bots.bot_id
    param_dict={

            'MID': 'luxrst14122371794696',
            'ORDER_ID': str(time.time()),
            'TXN_AMOUNT': str(amount),
            'CUST_ID': 'WEB',
            'INDUSTRY_TYPE_ID': 'Retail',
            'WEBSITE': 'WEBSTAGING',
            'CHANNEL_ID': 'WEB',
            'CALLBACK_URL':'http://127.0.0.1:8000/paytm/handlerequest/',

    }

    param_dict['CHECKSUMHASH']=checksum.generate_checksum(param_dict,MERCHANT_KEY)
    print(param_dict)
    return  render(request, 'paytm/paytm.html', {'param_dict': param_dict})
    # return render(request, 'shop/checkout.html')


@csrf_exempt
def handlerequest(request):
    form=request.POST
    response_dict={}
    print(form)
    for i in form.keys():
        response_dict[i]=form[i]
        print(i)
        if i== 'CHECKSUMHASH':
            Checksum=form[i]
    print(response_dict)
    verify=checksum.verify_checksum(response_dict, MERCHANT_KEY, Checksum)
    if verify:
        if response_dict['RESPCODE']=='01':
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
        else:
            print('order was not successful because'+response_dict['RESPMSG'])
            messages.error(request, f"Payment Unsuccessful because of {response_dict['RESPMSG']}")
            return redirect('index')

    return render(request,'paytm/paymentstatus.html',{'response':response_dict})