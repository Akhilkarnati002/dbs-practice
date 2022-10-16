from django.urls import path
from .views import Home, MoneyTransfer,SignUp,Login,AccountSetup
from django.contrib.auth.views import LogoutView
urlpatterns = [
   path('',Home.as_view(),name='home'),
   path('signup/',SignUp.as_view(),name='signup'),
   path('login/',Login.as_view(),name='login'),
   path('logout/',LogoutView.as_view(),name='logout'),
   path('accountsetup/',AccountSetup.as_view(),name='account'),
   path('moneytransfer/',MoneyTransfer.as_view(),name='moneytransfer'),
    
]