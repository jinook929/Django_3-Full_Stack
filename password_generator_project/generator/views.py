from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):
    x = list('abcdefghijklmnopqrstuvwxpyz')
    password = ''

    length = int(request.GET.get('length'))
    upper = request.GET.get('upper')
    number = request.GET.get('number')
    special = request.GET.get('special')

    if(upper == "on"):
        x.extend('ABCDEFGHIJKLMNOPQRSTUVWXYZ')    
    if(number == "on"):
        x.extend('0123456789')    
    if(special == "on"):
        x.extend('~!@#$%^&*()-=_+;<>,./?|')
    
    for i in range(length):
        password += random.choice(x) 
    return render(request, 'generator/password.html', { "password": password})


def about(request):
    return render(request, 'generator/about.html')