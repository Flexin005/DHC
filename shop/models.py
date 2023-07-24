from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)
    image1 = models.ImageField(upload_to='category', blank=True)
    image2 = models.ImageField(upload_to='category', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return str(self.name)



class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=True)
    image_url = models.CharField(max_length=1000000, blank=True)
    stock = models.IntegerField()
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0, null=True)
    best_seller = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def discounted_price(self):
        disprice = float(self.price * (1 - self.discount))
        return disprice

    def discounted_percentage(self):
        dispercent = f'{int((self.discount) * 100)}% off'
        return dispercent

    def __str__(self):
        return str(self.name)


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    data_added = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Cart'
        ordering = ['data_added']

    def __str__(self):
        return str(self.cart_id)


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    class Meta:
        db_table = 'CartItem'

    def sub_total(self):
        if self.product.discount > 0:
            return float(self.product.discounted_price() * self.quantity)
        else:
            return self.product.price * self.quantity

    def __str__(self):
        return str(self.product)


class Order(models.Model):
    token = models.CharField(max_length=250, blank=True)
    total = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='USD Order Total')
    emailAddress = models.EmailField(
        max_length=250, blank=True,  verbose_name='Email Address')
    created = models.DateTimeField(auto_now_add=True)
    billingName = models.CharField(max_length=250, blank=True)
    billingAddress1 = models.CharField(max_length=250, blank=True)
    billingCity = models.CharField(max_length=250, blank=True)
    billingPostcode = models.CharField(max_length=250, blank=True)
    billingCountry = models.CharField(max_length=250, blank=True)
    shippingName = models.CharField(max_length=250, blank=True)
    shippingAddress1 = models.CharField(max_length=250, blank=True)
    shippingCity = models.CharField(max_length=250, blank=True)
    shippingPostcode = models.CharField(max_length=250, blank=True)
    shippingCountry = models.CharField(max_length=250, blank=True)

    class Meta:
        db_table = 'Order'
        ordering = ['-created']

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.CharField(max_length=250)
    quantity = models.IntegerField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name='INR Price')
    discount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    class Meta:
        db_table = 'OrderItem'

    def discounted_price(self):
        disprice = float(self.price * (1 - self.discount))
        return disprice

    def sub_total(self):
        if self.discount > 0:
            return float(self.discounted_price() * self.quantity)
        else:
            return self.price * self.quantity


    def __str__(self):
        return str(self.product)


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=500)

    def __str__(self):
        return str(self.content)

class ad(models.Model):
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='ads', default='image')
    created = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'ad'
        verbose_name_plural = 'ads'

    def __str__(self):
        return str(self.name)


class bestoffer(models.Model):
    name = models.CharField(max_length=250)
    image1 = models.ImageField(upload_to='bestoffers', blank=True, default="image1")
    image2 = models.ImageField(upload_to='bestoffers', blank=True, default="image2")
    image3 = models.ImageField(upload_to='bestoffers', blank=True, default="image3")

    class Meta:
        ordering = ('name',)
        verbose_name = 'bestoffer'
        verbose_name_plural = 'bestoffers'

    def __str__(self):
        return str(self.name)

