from django.urls import path
from contacts import views

app_name = 'contact'
urlpatterns = [
    path('', views.contact_us,name='contact_us'),
]