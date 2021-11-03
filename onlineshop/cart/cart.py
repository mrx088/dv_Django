from shop.models import Item
from decimal import Decimal

SESSION_NAME = 'cart'
class Cart:


    def __init__(self,request):
        self.session = request.session
        cart = self.session.get(SESSION_NAME)
        if not cart :
            cart = self.session[SESSION_NAME] = {}        
        self.cart = cart

    def __iter__(self):
        products_ids = self.cart.keys()
        products = Item.objects.filter(id__in=products_ids)
        cart = self.cart.copy()
        for product in products :
            cart[str(product.id)]['product'] = product


        for item in cart.values():
            item['total_price'] = Decimal(item['price'])*item['quantity']
            yield item


    def add (self,product,quantity):
        product_id = str(product.id)
        product_dis = Item.objects.get(id=product.id)


        if product_id not in self.cart and product_dis.discount is not None:
            self.cart[product_id] = {'quantity':0, 'price':str(product.discount),}
        

        if product_id not in self.cart and product_dis.discount is None:
            self.cart[product_id] = {'quantity':0, 'price':str(product.price),}
        
        self.cart[product_id]['quantity'] += quantity

        self.save()



    def Delete_session(self,product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    
    def get_total_price(self):
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())




    def save(self):
        self.session.modified = True


    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())

    
    def clear(self):
        del self.session[SESSION_NAME]
        self.save()