from django import forms

class userforms(forms.Form):
    user_name= forms.CharField()
    first_name= forms.CharField()
    second_name= forms.CharField()
    