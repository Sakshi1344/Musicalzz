from django.shortcuts import render
# login imports
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='authenticate:login')
def home(request):
    return render(request,'Home.html')

def create(request):
    return render(request,'Create.html')

def card1(request):
    return render(request,'card1.html')

def card2(request):
    return render(request,'card2.html')

def index(request):
    return render(request,'index.html')
