from django.urls import path
from . import views
from django.urls import include


urlpatterns = [
    path("", views.home, name="ShopHome"),
    path("contact/", views.contact, name="ContactUs"),
    path("tradingview/", views.tradingview, name='tradingview'),
    path("query_message/", views.query_message, name='query_message'),
    path("bots/", views.bots, name="bots"),
    path("add_api/", views.add_api, name="add_api"),
    path("terms/", views.terms, name="terms"),
    path("error/", views.error, name="error"),
    path("signup", views.signup, name="signup"),
    path("handleLogin", views.handleLogin, name="handlelogin"),
    path("all_bots", views.all_bots, name="all_bots"),
    path("user_bots", views.user_bots, name="user_bots"),
    path("index", views.index, name="index"),
    path("settings", views.setting, name="settings"),
    path("checkout", views.checkout, name="checkout"),
    path("handleLogout", views.handleLogout, name="handleLogout"),
    path("withdraw", views.withdraw, name="withdraw"),
    path("resendOTP", views.resendOTP, name="resendOTP"),
    path("key", views.key, name="key"),
    path("forgot", views.forgot, name="forgot"),
    path("tradingview_webhook/<str:passphrase>", views.tradingview_webhook, name='tradingview_webhook'),

]
