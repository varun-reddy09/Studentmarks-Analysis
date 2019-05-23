#!/usr/bin/env python
from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Profile,SemPercentage,SemMarks
import os
# Create your views here.
# import matplotlib.pyplot as plt

@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get('password')
        user = User.objects.create_user(username=username,  password=password)
        print(user)
        user.is_staff = True
        user.save()
        login(request, user)
        return redirect(reverse('home'))


#login Page

def home(request):
    return render(request,'main/index.html')

# def analysis(request):
#
#     fig = plt.figure(figuresize=(5, 5))  # size in inches
#     # use plot(), etc. to create your plot.
#
#     x=[5,8,10]
#     y=[12,16,6]
#     plt.plot(x,y)
#     plt.title('Information')
#     plt.xlabel('X-axis')
#     plt.ylabel('Y-axis')
#
#     save_file = os.path.join('main/static/img/', 'fig1.png')
#
#     plt.savefig(save_file)
#     plt.close(fig)
#
#     return render(request,'main/analysis.html')

def loginform(request):
    return render(request,'main/login.html')


def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

def login_view(request):
    if request.method == 'POST':

        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse("home"))
        else:
            return HttpResponse("This User doesn't exist");
