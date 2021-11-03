from django.urls import path
from orders import views

app_name = 'orders'
urlpatterns = [
    path('create/', views.create,name='create'),
    path('detail/<int:order_id>/', views.detail,name='detail'),
]