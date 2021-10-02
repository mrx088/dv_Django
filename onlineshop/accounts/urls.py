from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.accounts_login,name='login'),
    path('rejister/', views.accounts_rejister,name='rejister'),
]
