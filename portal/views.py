from django.http.response import HttpResponseRedirect
from django.contrib import messages
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Person
from .forms import RegisterForm

# Create your views here.

def home(request): 
    return render(request, 'home.html')

def signup(request):
    if request.method == "POST":
        print("signup")
        profession = request.POST.get('profession')
    return render(request, 'signup.html',{'profession':profession})

def choice(request):
    return render(request, 'choice.html')

def login(request):
    print("strign func")
    if request.method == "POST":
        email = request.POST.get('email')
        password =  request.POST.get('password')
        profession = request.POST.get('profession')
        user=Person.objects.get(email=email)
        if user is not None:
            if user.password==password and user.profession==profession:
                print("strign")
                messages.info(request,'Logged in')
                return redirect('/') 
            else:
                print("strignsss")
                messages.info(request,'invalid credentials')
                return redirect('/')
        else:
            print("strign esle")
        
    return redirect('/')    
    
def register(request):
    print("register")
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)
            person.save()
        else: 
            form = RegisterForm()
    return redirect('/')

def teams(request):
    return render(request, 'home.html')