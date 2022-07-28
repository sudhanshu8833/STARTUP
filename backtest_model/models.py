from django.db import models

# Create your models here.

class strategy(models.Model):
    strategy_id=models.CharField(max_length=20,default="NONE")
    strategy_name=models.CharField(max_length=50,default="NONE")
    interval=models.CharField(max_length=20,default="1D")
    crypto=models.CharField(max_length=20,default="BTCUSDT")
    candle_type=models.CharField(max_length=20,default="ohlc")
    pyramiding=models.IntegerField(default=1)




class Conditions(models.Model):
    strategy_id=models.CharField(max_length=20,default="NONE")
    condition_type=models.CharField(max_length=20,default="INDICATOR")
    indicator=models.CharField(max_length=20,default="NONE")
    