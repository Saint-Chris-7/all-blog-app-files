from django.forms import ModelForm
from .models import Customers

class RegForm(ModelForm):
    class Meta:
        model= Customers
        fields= '__all__'