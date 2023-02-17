from django.urls import path
from . import views

app_name = 'accountApp'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('registration_success/', views.success, name='success'),
    path('login/', views.logintUser, name='loginUser'),
    path('logout/', views.logoutUser, name='logoutUser'),
]
