
from django.shortcuts import redirect, render , get_object_or_404
from .cart import Cart
from .forms import QuantityForm
from shop.models import Item , OrderItem
from django.contrib import messages
from django.views.decorators.http import require_POST
# Create your views here.


def shop_summary(reuqest):
    cart = Cart(reuqest)
    return render (reuqest,'cart/shop_summary.html',{'cart':cart,})




@require_POST
def cart_add(request,product_id):
    cart = Cart(request)
    product = get_object_or_404(Item,id=product_id)
    form = QuantityForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'])
    return redirect ('cart:shop_summary')





def cart_delete(request,product_id):
    cart = Cart(request)
    product = Item.objects.get(id=product_id)
    cart.Delete_session(product=product)
    messages.success(request,'You deleted succesfuly','info')
    return redirect ('cart:shop_summary')