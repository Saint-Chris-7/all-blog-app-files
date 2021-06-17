from django import forms
from .models import Authors,Articles

class authorform(forms.ModelForm):
    class Meta:
        model= Articles
        fields="__all__"