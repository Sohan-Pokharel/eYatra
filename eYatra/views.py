
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from . import views
from django.contrib.auth import authenticate ,logout, login 
from django.contrib.auth.decorators import login_required
from django.contrib import auth


def home(request):
    return render(request, 'home.html')

def things(request):
    return render(request, 'things.html')


@login_required
def destination(request):
    # user= request.user
    return render(request, 'destination.html')

def package(request):
    return render(request, 'package.html')

def register(request):
    if request.method=='POST':
         username = request.POST.get('username')
         email=request.POST.get('email')
         pass1=request.POST.get('password1')
         pass2=request.POST.get('password2')
         if pass1!=pass2:
              return HttpResponse("password and confirm password are not same")
         else:
             my_user=User.objects.create_user(username,email,pass1)
             my_user.save()
             return redirect('login')
    return render(request, 'register.html')

def login_user(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
           
        
        userobject=auth.authenticate(request, username=username, password=password)
            

        if userobject is not None:
          
            login (request,userobject)
            print("login succed")
          
            return redirect('home')
        else:
                print("user name and password incorrect")
             
    return render(request, 'login.html')

  
    