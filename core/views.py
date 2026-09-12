from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login 
from item.models import Item
# Create your views here.
def LandingView(request):
    return render(request, 'landing.html')


def SignUpView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})

def HomeView(request):
    items = Item.objects.all().order_by('-created_at')

    return render(request,'home.html',{'items':items})