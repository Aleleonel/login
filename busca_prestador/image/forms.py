from django import forms
from django.forms.widgets import ClearableFileInput

from .models import Imagens


class ImageForm(forms.ModelForm):
    fotos = forms.ImageField(widget=ClearableFileInput)

    class Meta:
        model = Imagens
        fields = ('titulo', 'fotos')


