from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm, ReportItemForm
from django.contrib.auth.decorators import login_required
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

@login_required
def HomeView(request):
    items = Item.objects.all().order_by('-created_at')

    return render(request,'home.html',{'items':items})

@login_required
def ReportItemView(request):
    if request.method == 'POST':
        form = ReportItemForm(request.POST,request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.reported_by = request.user
            item.status = 'open'
            item.save()
            return redirect('home')

    else:
        form = ReportItemForm()

    return render(request,'reportitem.html', {'form':form})


def ItemDetailsView(request,pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'details.html', {'item':item})