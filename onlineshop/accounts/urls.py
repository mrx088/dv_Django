from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


app_name = 'accounts'
urlpatterns = [
    path('reset/', views.Userresetpassword.as_view(),name='reset_password'),
    path('reset/done/', views.PasswordResetDone.as_view(),name='password_reset_done'),
    path('confirm/reset/<uidb64>/<token>/', views.password_reset_confirm.as_view(),name='password_reset_confirm'),
    path('confirm/done/', views.password_reset_complete.as_view(),name='password_reset_complete'),
    path('login/', views.accounts_login,name='login'),
    path('phonelogin/', views.accounts_phonelogin,name='phonelogin'),
    path('phonelogincheack/', views.accounts_phonelogincheack,name='phonelogincheack'),
    path('rejister/', views.accounts_rejister,name='rejister'),
    path('logout/', views.accounts_logout,name='logout'),
    path('dashboard/<int:user_id>', views.accounts_dashboard,name='dashboard'),
    path('users/contact', views.accounts_users,name='users'),
    path('follow/', views.follow_acc,name='follow'),
    path('unfollow/', views.unfollow_acc,name='unfollow'),
]
