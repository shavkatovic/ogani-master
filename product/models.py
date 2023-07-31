from tkinter.constants import CASCADE

from django.db import models
from django.db.models import CASCADE


class Product(models.Model):
    name = models.CharField(max_length=250)
    bio = models.TextField()
    description = models.TextField()
    quantity = models.PositiveIntegerField()
    shipping = models.CharField(max_length=250, null=True, blank=True)
    weight = models.DecimalField(max_digits=9, decimal_places=2)
    categories = models.ManyToManyField('product.Categories', 'products')


class Categories(models.Model):
    title = models.CharField(max_length=250)


class Image(models.Model):
    product = models.ForeignKey('product.Product', CASCADE, 'images')
    image = models.ImageField(upload_to='images/product')
