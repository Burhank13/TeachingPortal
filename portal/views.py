from django.http.response import HttpResponseRedirect
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
        profession = request.POST.get('profession')
    return render(request, 'signup.html',{'profession':profession})

def choice(request):
    return render(request, 'choice.html')

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password =  request.POST.get('password')
        profession = request.POST.get('profession') 
    return redirect('/')    
    
def register(request):
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