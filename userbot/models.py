from django.db import models

# Create your models here.
class BTCUSDT(models.Model):
    time=models.FloatField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()

class ETHUSDT(models.Model):
    time=models.FloatField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()

class SOLUSDT(models.Model):
    time=models.FloatField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()

class BNBUSDT(models.Model):
    time=models.FloatField()
    Open = models.FloatField()
    High = models.FloatField()
    Low = models.FloatField()
    Close = models.FloatField()