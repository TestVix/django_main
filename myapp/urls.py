
from django.urls import path
from . import views
app_name = 'myapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('testlarim/', views.testlarim, name='testlarim'),
    path('admin_user/', views.admin_user, name='admin_user'),
]
