
from django.urls import path
from .views import *

urlpatterns = [
    path('',signup,name='Login'),
    path('signin/',signin, name='signin'),
    path('signup/',my_form,name="myform"),
    path('submit/',submit,name="submit"),
    path('read/',read,name="read"),
    path('update/<int:pk>',update,name="update"),
    path('updated/<int:pk>',updatedata,name="updatedata"),
    path('delete/<int:pk>',deldata,name="deldata"),
    path('home/<int:pk>',home,name='home'),
    path('transfer/<int:pk>',transfer,name='tranfer')

]
