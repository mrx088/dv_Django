from django.db import models
from django.conf import settings
from django.urls import reverse
from django.http import request

# Create your models here.

class Category (models.Model) :
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True)


    def __str__(self):
        return self.title


class Item (models.Model) :

    item_label = (
        ('D','danger'),
        ('P','primary'),
        ('S','secondary'),
    )
    name  = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150,unique=True,)
    photo = models.ImageField(upload_to='products/%Y/%M/%d')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    label = models.CharField(max_length=1,choices=item_label)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    published = models.BooleanField(default=True)
    discount = models.IntegerField(blank=True,null=True)
    number = models.IntegerField(default=1)
    exist = models.BooleanField(default=True)
    


    def __str__(self):
        return self.name

    def get_absolute_url (self):
        return reverse('shop:detail',args={self.slug,})

    def get_absolute_url2 (self):
        return reverse('shop:add_to_cart',args={self.slug,})


class OrderItem (models.Model):
    order       =   models.ForeignKey('Order',on_delete=models.CASCADE,related_name='items')
    product     =   models.ForeignKey(Item,on_delete=models.CASCADE,related_name='order_item')
    price       =   models.DecimalField(max_digits=10,decimal_places=2)
    quantity    =   models.PositiveSmallIntegerField(default=1)


    def __str__(self):
        return str(self.id)



    def get_cost(self):
        return self.price * self.quantity

    def get_price (self) :
        return self.quantity * self.product.price

    def get_discount_price (self) :
        return self.quantity * self.product.discount



class Order (models.Model):
    user        =   models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='orders')
    created     =   models.DateTimeField(auto_now_add=True)
    updated     =   models.DateTimeField(auto_now=True)
    paid        =   models.BooleanField(default=False)



    class Meta:
        ordering = ('-created',)


    def __str__(self):
        return f'{self.user}-{str(self.id)}'


    
    def get_total_price(self):
        return sum(item.get_cost() for item in self.items.all())
