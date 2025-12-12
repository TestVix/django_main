from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'simple_user/home.html')

def login(request):
    return render(request, 'simple_user/login.html')
def register(request):
    return render(request, 'simple_user/register.html')