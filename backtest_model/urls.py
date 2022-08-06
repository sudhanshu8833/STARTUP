from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path("backtesting_instruments", views.backtest, name="backtesting"),


]
