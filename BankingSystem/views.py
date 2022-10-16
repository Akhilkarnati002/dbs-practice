from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView

from BankingSystem.models import CustomUser, Profile
from .forms import CustomUserCreationForm,AccountCreationform
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.

class Home(DetailView):
    model=Profile
    context_object_name= "var"
    template_name = "home.html"

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('account')
    
    
class Login(LoginView):
    template_name = 'registration/login.html'

class AccountSetup(UpdateView):
    form_class= AccountCreationform
    template_name = 'registration/account.html'
    success_url = reverse_lazy('home')
    '''def get_object(self,**kwargs):
        var=CustomUser.all()
        if AccountSetup.get(user_id=self.kwargs["pk"]):
            return AccountSetup.get(user_id=self.id)
        else:
            x=AccountSetup(user_id=self.id)
            x.save()
            return AccountSetup.get(user_id=self.id)'''


