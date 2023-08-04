from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from goods.models import Category, Product


class ProductCreateForm(forms.Form):
    categories = forms.ModelChoiceField(queryset=Category.objects.all())
    title = forms.CharField(max_length=150)
    image = forms.ImageField()
    description = forms.CharField(widget=forms.Textarea())
    price = forms.FloatField()
    discount = forms.FloatField(required=False)
    quantity = forms.IntegerField()
    size = forms.CharField(max_length=150)
    weight = forms.FloatField(required=False)
    rate = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])


class CategoryCreateForm(forms.Form):
    title = forms.CharField(max_length=128)


class ReviewCreateForm(forms.Form):
    products = forms.ModelChoiceField(queryset=Product.objects.all())
    image = forms.ImageField(required=False)
    video = forms.FileField(required=False)
    text = forms.CharField(widget=forms.Textarea())
    rate = forms.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)])
