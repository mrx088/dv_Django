from django.shortcuts import redirect, render , get_object_or_404
from shop.models import Order,OrderItem
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def create(request):
    cart = Cart(request)
    order= Order.objects.create(user=request.user)
    for item in cart :
        OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
    cart.clear()
    return redirect ('orders:detail', order.id )




@login_required
def detail(request,order_id):
    order = get_object_or_404(Order,pk=order_id)
    return render (request, 'orders/index.html', {'order':order})