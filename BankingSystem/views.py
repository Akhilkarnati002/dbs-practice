from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView
from .forms import CustomUserCreationForm,AccountCreationform
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.

class Home(TemplateView):
    template_name = "home.html"

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/sign_up.html'
    success_url = reverse_lazy('account')
    
    
class Login(LoginView):
    template_name = 'registration/login.html'

class AccountSetup(CreateView):
    form_class= AccountCreationform
    template_name = 'registration/account.html'
    success_url = reverse_lazy('home')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AccountSetup, self).form_valid(form)
    
