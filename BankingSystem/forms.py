from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser,AccountType,Profile
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('phonenumber','aadhar_card','pan_card','dob')
    
class AccountCreationform(ModelForm):
    class Meta(ModelForm):
        model=Profile
        fields=("account_type_id",)
        #Widgets={"user_id":forms.HiddenInput()}

class MoneyTransferForm(ModelForm):
    money_transfer = forms.IntegerField()
    class Meta(ModelForm):
        model=Profile
        fields=("user_id","money_transfer")

