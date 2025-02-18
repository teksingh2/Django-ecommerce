from django.db import models
from typing import Reversible
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user=models.OneToOneField(User,null=False,blank=False,on_delete=models.CASCADE)
    #phone_field=models.CharField(max_length=12)

    def __str__(self):
        return self.user.username
    

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    desc = models.TextField()
    price = models.FloatField(default=0.0)
    product_available_count = models.IntegerField(default=0)
    img = models.ImageField(upload_to="images/")

    def get_add_to_cart_url(self):
        return Reversible("core:add-to-cart", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name