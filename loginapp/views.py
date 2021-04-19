from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.urls import reverse
from django.views import View
from django.http import HttpResponseRedirect
# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('schedule_index'))

class loginview(View):
    def log_in(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return render(request,'loginapp/login.html',{'msg' : "Invalid data entered"})
        return render(request,'loginapp/login.html')

class logoutview(View):
    def log_out(request):
        logout(request)
        return render(request,'loginapp/user.html',{'msg':"Logged out"})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username = username, password = password)
            return HttpResponseRedirect(reverse('login'))
        except:
            return render(request, 'loginapp/register.html')
    return render(request, 'loginapp/register.html')
