from django.shortcuts import render

from .models import MyModel
from .forms import MyForm

# Create your views here.
def signup(request):
    return render(request,'index.html')
def signin(request):
    return render(request,'login.html')





def my_form(request):
  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'index.html', {'form': form})