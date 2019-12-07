from django import forms
from .models import Solicitacao

class SoliForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = '__all__'

