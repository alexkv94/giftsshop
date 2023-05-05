from django.conf import settings
from .models import Product

class Cart(object):
    def __init__(self, request):
        # sets an instance variable on the Cart object
        self.session = request.session

        # gets the user's cart data from the session if there is
        cart = self.session.get(settings.CART_SESSION_ID)

        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    # Makes the cart object iterable
    def __iter__(self):
        for p in self.cart.keys():
            # retrieves the product for the cart item
            self.cart[str(p)]['product'] = Product.objects.get(id=p)

        for item in self.cart.values():
            # calculates the total price of cart items
            item['total_price'] = int(item['product'].price * item['quantity'])

            yield item

    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def add(self,product_id, quantity=1, update_quantity=False):
        product_id = str(product_id)

        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': quantity, 'id': product_id}

        if update_quantity:
            self.cart[product_id]['quantity'] += int(quantity)

            self.save()

    def get_total_cost(self):
        for p in self.cart.keys():
            self.cart[str(p)]['product'] = Product.objects.get(id=p)

        return int(sum(item['product'].price * item['quantity'] for item in self.cart.values()))