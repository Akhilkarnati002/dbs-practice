from email import message
from django.http import HttpResponse
from django.shortcuts import render,redirect

from .models import MyModel, Profile


# Create your views here.
def signup(request):
    return render(request,'index.html')
def signin(request):
    return render(request,'login.html')





def my_form(request):
  if request.method == "POST":
      Username = request.POST['username']
      Email = request.POST['email']
      Password = request.POST['password']
      Cpassword = request.POST['cpassword']
      form = MyModel(username=Username,email=Email,password=Password)
      form.save()
      return render(request, 'login.html')
  else:
    return HttpResponse("invalid data")  
      


def submit(request):
    if request.method == "POST":
        user = request.POST['username']
        pass1 = request.POST['pass']
        try:
            k=MyModel.objects.get(username=user)
        except:
            return HttpResponse("login Failed invalid credentials")
        if k:  
            if k.password == pass1 :
                request.session['username']=k.username
                request.session['email']=k.email
                return redirect('/read')
            else:
                return HttpResponse("login Failed invalid credentials")

           
        else:    
            return HttpResponse("login Failed invalid credentials")
            

def read(request):
    f=MyModel.objects.all()
    return render(request,'read.html',{ "data":f })

def update(request, pk):
    m=MyModel.objects.get(id=pk)
    return render(request,'update.html',{ "data":m })

def updatedata(request,pk):
    k=MyModel.objects.get(id=pk)
    k.username = request.POST['username']
    k.email = request.POST['email']
    k.save()

    return redirect("/read")


def deldata(request,pk):
    d=MyModel.objects.get(id=pk)
    d.delete()
    return redirect("/read")

def home(request,pk):
    a= Profile.objects.get(id=pk)
    return render(request,'home.html',{'data': a})

def transfer(request,pk):
    if request.method=="POST":
        toacc=request.POST['toaccount']
        amount=request.POST['amount']
        m=MyModel.objects.get(id=pk)
        if m.curr_bal<amount:
            return HttpResponse("insufficient amount")
        else:
            m.curr_bal-=amount
            m.save()
            n=MyModel.objects.get(id=toacc)
            n.curr_bal+=amount
            n.save()
    return redirect('/home.html')    
            
