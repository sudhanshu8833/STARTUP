from django.db import models
from django.db.models.fields import DateField, IntegerField

class User1(models.Model):
    username=models.CharField(max_length=50,default='SOME STRING')
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=25)
    phone=models.IntegerField(default='999')
    fullname=models.CharField(max_length=50,default='SOME STRING')
    binance_API_keys=models.CharField(max_length=100,default='SOME STRING')
    binance_Secret_Keys=models.CharField(max_length=100,default='SOME STRING') 


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
    description=models.CharField(max_length=5000) 
    title=models.CharField(max_length=50)

class orders(models.Model):
    symbol = models.CharField(max_length=20)
    Price_in = models.FloatField()
    time_in = models.DateTimeField()
    order_type = models.CharField(max_length=20)
    bot = models.CharField(max_length=20)