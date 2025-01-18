from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Country(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=255)



class Product(BaseModel):
    title = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    discount = models.IntegerField(null=True, blank=True)
    rate = models.IntegerField()
    image = models.ImageField(upload_to='products/images/')
    full_description = models.TextField()
    category = models.ManyToManyField(Category, related_name='products')
    country = models.ManyToManyField(Country, related_name='products')
    size = models.ManyToManyField(Size, related_name='products')
    tag = models.ManyToManyField(Tag, related_name='products')


class Explanation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='explanations')
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name='explanations')
    comment = models.TextField()



class User(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.IntegerField()

 

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    total_amount = models.IntegerField()
    status = models.CharField(max_length=50)



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    price = models.IntegerField()
    quantity = models.IntegerField()


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

