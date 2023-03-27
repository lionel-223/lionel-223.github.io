from django import forms
from .models import Mes_Articles

class parametres(forms.Form):
    param = forms.CharField(label='param', max_length=100)
