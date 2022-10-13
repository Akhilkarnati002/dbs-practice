
from django.urls import path
from .views import *

urlpatterns = [
    path('',signup,name='Login'),
    path('signin/',signin, name='signin')
]
