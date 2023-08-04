from django.contrib import admin

from goods.models import Product, Category, Review


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'categories', 'price', 'quantity', 'rate', 'created_date',)
    sortable_by = ('title', 'categories', 'price', 'rate', 'created_date',)
    list_display_links = ('id', 'title',)
    list_filter = ('categories', 'price', 'rate',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_date',)
    sortable_by = ('title', 'created_date',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'products', 'rate', 'created_date',)
    sortable_by = ('products', 'rate', 'created_date',)
    list_display_links = ('id', 'products',)
