from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def register(request):
    return render(request, 'synerd/register.html')

def login(request):
    return render(request, 'synerd/login.html')

def dashboard(request):
    return render(request, 'synerd/dashboard.html')

def home(request):
    return render(request, 'synerd/index.html')