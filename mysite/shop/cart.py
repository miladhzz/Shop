from decimal import Decimal
from django.conf import settings
from .models import Product


class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, count=1, update_count=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'count': 0,
                                     'price': str(product.price)}
        if update_count:
            self.cart[product_id]['count'] = count
        else:
            self.cart[product_id]['count'] += count
        self.save()

    def save(self):
        # update the session count
        self.session[settings.CART_SESSION_ID] = self.cart
        # make the session as 'modified' to make sure it is saved
        self.session.modified = True

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def __iter__(self):
        # Iterate over the items in cart and get the products from db
        product_ids = self.cart.keys()
        # get the product object and add them to the cart
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            self.cart[str(product.id)]['product'] = product

        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['count']
            yield item

    def __len__(self):
        # count all item in the cart
        return sum(item['count'] for item in self.cart.values())

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['count'] for item in self.cart.values())

    def clear(self):
        # empty cart
        self.session[settings.CART_SESSION_ID] = {}
        self.session.modified = True
