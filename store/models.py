from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super(Customer, self).save(*args, **kwargs)

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    price = models.DecimalField(max_digits=7, decimal_places= 2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)
    
    @property
    def imgURL(self):
        try:
            url = self.image.url 
        except:
            url = ''
        return url

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=30, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

 
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    data_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product.name)
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,null=True, blank=True)
    address = models.CharField(max_length=50, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    zipcode = models.CharField(max_length=50, null=False)
    data_added = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return str(self.address)

    