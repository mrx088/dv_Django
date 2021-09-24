from django.urls import path
from . import views


app_name    =   'shop'


urlpatterns = [
    path('', views.shops, name='shops'),
    path('detail/product/<slug:slug>', views.shops_detail, name='detail'),
    path('add_to_cart/<slug:slug>', views.add_to_cart, name='add_to_cart'),
]
