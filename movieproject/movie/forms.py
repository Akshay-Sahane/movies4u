from django import forms
from .models import HMovie
from .models import BMovie

class BForm(forms.ModelForm):
    CHOICES=(
        ('Action','action'),('Romantic','romantic'),('Crime','crime'),('Thriller','thriller')
        )
    movieType = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    movieDescription=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3,'cols':25}))
    class Meta:
        model=BMovie
        fields="__all__"
        widgets={
            'foodName':forms.TextInput(attrs=
            {'class':'form-control'})
        }

class HForm(forms.ModelForm):
    CHOICES=(
        ('Action','action'),('Romantic','romantic'),('Crime','crime'),('Thriller','thriller')
        )
    movieType = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    movieDescription=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':3,'cols':25}))
    class Meta:
        model=HMovie
        fields="__all__"
        widgets={
            'foodName':forms.TextInput(attrs=
            {'class':'form-control'})
        }