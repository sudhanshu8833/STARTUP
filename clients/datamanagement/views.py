import logging
import telepot
from clients.datamanagement.helpful_scripts.background_functions import working_days
from django.shortcuts import render
from .helpful_scripts.strategy import *

# Create your views here.
from django.contrib import messages
import threading
from clients.datamanagement.models import strategy
import random
import string
from .models import positions,  strategy
from clients.datamanagement.helpful_scripts.background_functions import *
from smartapi import SmartConnect


logger = logging.getLogger('dev_log')

# bot = telepot.Bot("5448843199:AAEKjMn2zwAyZ5tu8hsLIgsakxoLf980BoY")
# bot.getMe()
sleep_time=0
# working_day_calculation(0)
def data_calculation(request):
    global obj

    print("#############")

    logger.info("updated the system")
    t = threading.Thread(target=working_day_calculation, args=[0])
    t.setDaemon(True)
    t.start()

    print("#############")
    return render(request, "index.html")


def index(request):

    strategy1=strategy.objects.get(username="testing")
    return render(request, "index.html",{'list':strategy1})







def position(request):

    position = positions.objects.filter(status="OPEN")


    return render(request, "position.html",    {
        'list': position
    })


def closed_positions(request):

    position = positions.objects.filter(status="CLOSED")


    return render(request, "closed_position.html",    {
        'list': position
    })


def start_strategy(request):
    global sleep_time
    print(request)
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

    if request.method == "POST":

        lot = request.POST['lots']
        
        weeekly_expiry=request.POST['weekly_expiry']
        monthly_expiry=request.POST['monthly_expiry']


        strategy1=strategy.objects.get(username="testing")

       
        strategy1.angel_api_keys=request.POST['angel_api_keys']
        strategy1.angel_client_id=request.POST['angel_client_id']
        strategy1.angel_password=request.POST['angel_password']

        strategy1.lots=request.POST['lots']
        strategy1.weekly_expiry=request.POST['weekly_expiry']
        strategy1.monthly_expiry=request.POST['monthly_expiry']
        strategy1.bot=request.POST['bot']
        strategy1.paper=request.POST['paper']

        strategy1.save()


            
        t = threading.Thread(target=do_something, args=[strategy1])
        t.setDaemon(True)
        t.start()

        return render(request, "index.html",{'list':strategy1})



    strategy1=strategy.objects.get(username="testing")
    return render(request, "index.html",{'list':strategy1})

def do_something(strategy):

    print("$#################@@@@@@@@")
    # try:
    strat = run_strategy(strategy)
    print("kdjflkdjfl;kdj;ls;lsdkl;sdk;lsdkls;dks;l")
    value=strat.run()
    if value!=None:
        return value





def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))
