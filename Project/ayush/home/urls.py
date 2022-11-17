from django.contrib import admin
from django.urls import path

from home import views
urlpatterns = [
    path("",views.home,name='home'),
    path("about",views.about,name='about'),
    path("seller",views.seller,name='seller'),
    path("buyer",views.buyer,name='buyer'),
    path("contact",views.contact,name='contact'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("seller_interface",views.seller_interface,name='seller_interface'),
    path("login_buy",views.login_buy,name="login_buy"),
    path("buyer_interface",views.buyer_interface,name="buyer_interface"),
    path('update/<int:id>', views.update, name='update'),
    path('update/updaterecord/<int:id>', views.updaterecord, name='updaterecord'),
    path("home",views.home,name='home'),
    path("adm",views.adm,name='adm')
]
