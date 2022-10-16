from django.shortcuts import render
from django.views.generic import TemplateView,CreateView,UpdateView,DetailView,View

from BankingSystem.models import CustomUser, Profile
from .forms import CustomUserCreationForm,AccountCreationform,MoneyTransferForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

# Create your views here.

class Home(View):
    def get(self,request):
        template_name = "home.html"
        try:
            details = Profile.objects.get(user_id=request.user.id)
        except:
            details=""
        return render(request, template_name, {"id":details})


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


class MoneyTransfer(CreateView):
    form_class = MoneyTransferForm
    template_name = 'moneytransfer.html'
    success_url = reverse_lazy('home')

    def get(self,request):
        template_name = 'moneytransfer.html'
        error=""
        return render(request, template_name,{"error":error,"form":MoneyTransferForm})
    
    def post(self,request):
        my_data = request.POST 
        money_transfer=int(my_data.money_transfer[0])
        user1=Profile.objects.get(user_id=request.user.id)
        user2=Profile.objects.get(user_id=int(my_data['user_id'][0]))
        template_name = 'moneytransfer.html'
        if money_transfer <= user1.current_balance:
             user1.current_balance-= money_transfer
             user1.save()
             user2.current_balance+= money_transfer
             user2.save()

        else:
            error="Money Excced the current balance"
            return render(request, template_name,{"error":error}) 