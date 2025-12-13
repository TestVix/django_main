from django.shortcuts import render
# from jwt_auth import jwt_required
from django_main.jwt_auth import jwt_required
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import AuthUser, Testlar
from django_main.settings import fast_api_account_domain
# from django_main.auth_backend import a
# Create your views here.
@jwt_required
def home(request):

    # user = AuthUser.objects.all()
    # for u in user:
    #     print(u.username, flush=True)
    # print('login', request.user_jwt)
    # login_s = 
    print(request.user_jwt, flush=True)
    if request.user_jwt:
        print('user authenticated', flush=True)
    # jwt_required(request.)
        return render(request, 'user/home.html')
        # return render(request, 'simple_user/home.html')
    else:
        print('user not authenticated', flush=True)
        return render(request, 'simple_user/home.html', {'fast_api_account_domain': fast_api_account_domain})

def login(request):
    return render(request, 'simple_user/login.html', {'fast_api_account_domain': fast_api_account_domain})
def register(request):
    return render(request, 'simple_user/register.html', {'fast_api_account_domain': fast_api_account_domain})


@jwt_required
def testlarim(request):
    print(request.user_jwt, flush=True)
    user_id = AuthUser.objects.get(username=request.user_jwt).id
    testlar = Testlar.objects.filter(user_id = user_id).all()
    return render(request, 'user/testlarim.html' , {
        'testlar': testlar
    })