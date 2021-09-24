from django.urls import path
from . import views


app_name    =   'cart'


urlpatterns = [
    path('cart/detail', views.shop_summary, name='shop_summary'),
    path('cart/<int:product_id>', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>', views.cart_delete, name='cart_delete'),
]
