from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
# login imports
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
# Create your views here.


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('note:home'))
            else:
                return HttpResponse("User is Not active")
        else:
            return HttpResponseRedirect(reverse('authenticate:login'))
    return render(request,'Login.html')

def user_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        user = User(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.save()
        return HttpResponseRedirect(reverse('note:home'))
    return render(request,'SignIn.html')

def user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect(reverse('note:index'))




