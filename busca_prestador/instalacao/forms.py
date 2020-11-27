from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Instalacao


class InstalacaoForm(forms.ModelForm):
    foto = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Instalacao
        fields = '__all__'

