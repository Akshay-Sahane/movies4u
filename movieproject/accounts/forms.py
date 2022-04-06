from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import MyUser

class UserForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('first_Name','last_Name','mobile_Number','password1','password2','user_Role')
        widgets={
            'first_Name':forms.TextInput(attrs={'class':'form-control'}),
            'last_Name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_Number':forms.NumberInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'user_Role':forms.HiddenInput(attrs={'value':'customer','m':'1'}),
               }

class AdminForm(UserCreationForm):
    class Meta:
        model=MyUser
        fields=('first_Name','last_Name','mobile_Number','password1','password2','user_Role')
        widgets={
            'first_Name':forms.TextInput(attrs={'class':'form-control'}),
            'last_Name':forms.TextInput(attrs={'class':'form-control'}),
            'mobile_Number':forms.NumberInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
            'user_Role':forms.HiddenInput(attrs={'value':'customer','m':'1'}),
        }

