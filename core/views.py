from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib.auth import login 
# Create your views here.
def LandingView(request):
    return render(request, 'landing.html')


def SignUpView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form':form})

def LoginView(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})
