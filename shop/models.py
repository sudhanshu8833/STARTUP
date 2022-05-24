from django.db import models
from django.db.models.fields import DateField, IntegerField
from django.contrib.auth.models import User

class User1(models.Model):
    username=models.CharField(max_length=50,default='SOME STRING')
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    phone=models.IntegerField(default='999')
    fullname=models.CharField(max_length=50,default='SOME STRING')
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    free=models.IntegerField(default=1)
    profits=models.FloatField(default=0)
    symbols_used=models.CharField(max_length=80,default="{'BTCUSDT': 100, 'BNBUSDT': 0, 'SOLUSDT': 0, 'BNBUSDT': 0}")
    Total_transaction=models.FloatField(default=0) 
    Total_invested=models.FloatField(default=0)
    Max_drawdown=models.FloatField(default=0)
    winning=models.IntegerField(default=100)
    # bots_owned=models.CharField(max_length=20,default=0)



class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField()

class BOT1(models.Model):
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()

    

class BOT2(models.Model):
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()


class BOT3(models.Model):
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()


class BOT4(models.Model):
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING')
    Expiry_date=models.DateField()
    email=models.EmailField(max_length=50)
    Max_loss=models.IntegerField()

class BOT(models.Model):
    bot_id=models.IntegerField(default=0)
    Price=models.IntegerField()
    subscription_time=models.CharField(max_length=100) 
    description=models.CharField(max_length=500) 
    title=models.CharField(max_length=50)
    profits=models.FloatField(default=10)
    symbols_used=models.CharField(max_length=80,default="{'BTCUSDT': 1, 'BNBUSDT': 1, 'SOLUSDT': 1, 'BNBUSDT': 1}")
    Total_transaction=models.FloatField(default=0)
    Total_invested=models.FloatField(default=0)
    Max_drawdown=models.FloatField(default=0)
    winning=models.IntegerField(default=100)
    Total_trades=models.IntegerField(default=0)

class orders(models.Model):
    symbol = models.CharField(max_length=20)
    Price_in = models.FloatField()
    time_in = models.DateTimeField()
    order_type = models.CharField(max_length=20)
    bot = models.IntegerField()




