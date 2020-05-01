from django.shortcuts import render
from django.http import HttpResponse
from backend.models import Subscriber, UserInfo

# Create your views here.
def register(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('address1') and request.POST.get('address2') and request.POST.get('city') and request.POST.get('state') and request.POST.get('zipcode') and request.POST.get('employername'):
            userinfo = UserInfo()
            userinfo.username = request.POST.get('username')
            userinfo.password = request.POST.get('password')
            userinfo.firstname = request.POST.get('firstname')
            userinfo.middlename = request.POST.get('middlename')
            userinfo.lastname = request.POST.get('lastname')
            userinfo.email = request.POST.get('email')
            userinfo.address1 = request.POST.get('address1')
            userinfo.address2 = request.POST.get('address2')
            userinfo.city = request.POST.get('city')
            userinfo.state = request.POST.get('state')
            userinfo.zipcode = request.POST.get('zipcode')
            userinfo.employername = request.POST.get('employername')
            userinfo.save()

            return render(request, 'synerd/register.html')

    else:

        return render(request, 'synerd/register.html')

def login(request):
    return render(request, 'synerd/login.html')

def dashboard(request):
    return render(request, 'synerd/dashboard.html')

def home(request):
    return render(request, 'synerd/index.html')

def members(request):
    getsubscriber = Subscriber.objects.all()
    return render(request, 'synerd/members.html', {'getsubscriber':getsubscriber})

def createpost(request):
    if request.method == 'POST':
        if request.POST.get('username') and request.POST.get('password') and request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('email') and request.POST.get('address1') and request.POST.get('address2') and request.POST.get('city') and request.POST.get('state') and request.POST.get('zipcode') and request.POST.get('employername'):
            userinfo = UserInfo()
            userinfo.username = request.POST.get('username')
            userinfo.password = request.POST.get('password')
            userinfo.firstname = request.POST.get('firstname')
            userinfo.middlename = request.POST.get('middlename')
            userinfo.lastname = request.POST.get('lastname')
            userinfo.email = request.POST.get('email')
            userinfo.address1 = request.POST.get('address1')
            userinfo.address2 = request.POST.get('address2')
            userinfo.city = request.POST.get('city')
            userinfo.state = request.POST.get('state')
            userinfo.zipcode = request.POST.get('zipcode')
            userinfo.employername = request.POST.get('employername')
            userinfo.save()