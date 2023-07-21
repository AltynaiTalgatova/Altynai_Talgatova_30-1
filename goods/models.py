from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, null=True)
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField()
    size = models.CharField(max_length=15)
    weight = models.FloatField(blank=True, null=True)
    rate = models.FloatField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
