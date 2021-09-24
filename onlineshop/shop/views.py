from django.shortcuts import redirect, render,get_object_or_404
from .models import Item, Order, OrderItem
from django.conf import settings
from django.utils import timezone
from cart.forms import QuantityForm

# Create your views here.



def shops (request) :

    items = Item.objects.all()
    return render(request,'shop/home.html',{'items':items})


def shops_detail (request,slug) :
    item = get_object_or_404(Item,slug=slug)
    form = QuantityForm()
    return render(request,'shop/detail.html',{'item':item,'form':form})

def add_to_cart (request,slug) :
    item = get_object_or_404(Item,slug=slug)
    order_item ,created= OrderItem.objects.get_or_create(item=item,user=request.user,ordered=False)
    order_qs= Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity +=1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,orderd_date=ordered_date)
        order.items.add(order_item)

    return redirect('shop:shops')