from re import template
from unicodedata import name
from django.urls import path
from .views import *
from django.views.generic.base import TemplateView

urlpatterns = [
    path("register-admin",register_admin,name="RegisterAdmin"),
    path("register-customer",register_customer,name="RegisterCustomer"),
    path("login",mylogin,name="Login"),
    path("logout",mylogout,name="Logout"),
    path('review',review,name="review"),
    path('preset',TemplateView.as_view(template_name="accounts/preset.html"),name="preset"),
    path('sendotp',sendotp,name="sendotp"),
    path('otpget',TemplateView.as_view(template_name='accounts/otp.html'),name="otpget"),
    path("setpassword",setpassword,name="setpassword"),
    path('otp',getotp,name="otp"),
]