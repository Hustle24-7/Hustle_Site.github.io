from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from Hustle import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .forms import MyForm

# Create your views here.
def index(request):
    return redirect('home')

def home(request):
    sending = 0
    print(make_password("Venkata@7854"))
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        body = request.POST.get('message')
        sending = 1
        body = body+'\n'+name+': '+email
        try:
            sender = settings.EMAIL_HOST_USER
            receiver = 'hustle247.clan@gmail.com'
            EmailMessage(sub,body,sender,[receiver]).send()
            sending = 3
        except:
            sending = 2
        print(name, email, sub, body)
    return render(request,'Contact/index.html', {'sending':sending})

def portfolio(request):
    return render(request, 'Contact/portfolio-details.html')

def portal(request):
    return render(request, 'Contact/portal.html')

def blog(request):
    return render(request, 'Contact/blog-single.html')

def register(request):
    if request.method == 'POST':
        data = MyForm(request.POST)
        try:
            if data.is_valid():
                data.save()
            else:
                return HttpResponse("Please enter valid data")
        except:
            print("error")
    form = MyForm()
    return render(request, 'Contact/register.html', {'form': form})