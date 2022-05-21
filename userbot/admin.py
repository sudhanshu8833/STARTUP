from userbot.models import BNBUSDT, BTCUSDT, ETHUSDT, SOLUSDT
from django.contrib import admin
from . import views
# Register your models here.
admin.site.register(BTCUSDT)
admin.site.register(ETHUSDT)
admin.site.register(SOLUSDT)
admin.site.register(BNBUSDT)