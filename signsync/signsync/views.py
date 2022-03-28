from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import CreateUserForm
def index(request):
    return render (request , 'index.html')

def home(request):
    return render (request , 'home.html')
    
def login1(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html')
        else:
            messages.info(request,'Username OR password is incorrect')

    return render (request , 'login.html')

# def logoutUser(request):
#     logout(request)
#     return redirect('login.html')


def register(request):
    form=CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login1')
    context={'form':form}
    return render (request , 'register.html',context)