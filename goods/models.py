from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Category(models.Model):
    title = models.CharField(max_length=128)
    created_date = models.DateTimeField(auto_now_add=True)


class Product(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    description = models.TextField()
    price = models.FloatField()
    discount = models.FloatField(blank=True, null=True)
    quantity = models.IntegerField()
    size = models.CharField(max_length=150)
    weight = models.FloatField(blank=True, null=True)
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    """categories"""
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)


class Review(models.Model):
    image = models.ImageField(blank=True, null=True)
    video = models.FileField(blank=True, null=True)
    text = models.TextField()
    rate = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)

    """products"""
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
