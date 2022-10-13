from django import forms
from .models import MyModel

class MyForm(forms.ModelForm):
  class Meta:
    model = MyModel
    fields = ["username", "email","password","cpassword","firstname"]
    labels = {'username': "Name", "email": "E-mail","password":"Password","cpassword":"Confirm Password"}