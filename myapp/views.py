from django.shortcuts import render
# from jwt_auth import jwt_required
from django_main.jwt_auth import jwt_required
# Create your views here.
@jwt_required
def home(request):
    print('login', request.user_jwt)

    return render(request, 'simple_user/home.html')

def login(request):
    return render(request, 'simple_user/login.html')
def register(request):
    return render(request, 'simple_user/register.html')