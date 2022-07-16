from shop.models import User1
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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