from django.db.models import Q
from django.shortcuts import render, redirect

from goods.models import Product, Category, Review
from goods.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm

from goods.constants import PAGINATION_LIMIT


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search_text:
            products = products.filter(Q(title__icontains=search_text) |
                                       Q(description__icontains=search_text))

        """Pagination"""
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page+1)
        }

        return render(request, 'products/products.html', context=context_data)


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()

        context_data = {
            'categories': categories
        }

        return render(request, 'products/categories/categories.html', context=context_data)


def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    if request.method == 'GET':

        context_data = {
            'product': product,
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context_data)

    if request.method == 'POST':
        if request.user.is_authenticated:
            data, files = request.POST, request.FILES
            form = ReviewCreateForm(data, files)

            if form.is_valid():
                Review.objects.create(
                    products=product,
                    image=form.cleaned_data.get('image'),
                    video=form.cleaned_data.get('video'),
                    text=form.cleaned_data.get('text'),
                    rate=form.cleaned_data.get('rate'),
                )
                return redirect('/products/')

            return render(request, 'products/detail.html', context={
                'form': form
            })

        return redirect('/users/login')


def product_create_view(request):
    if request.user.is_authenticated:

        if request.method == 'GET':

            context_data = {
                'form': ProductCreateForm
            }

            return render(request, 'products/create.html', context=context_data)

        if request.method == 'POST':
            data, files = request.POST, request.FILES
            form = ProductCreateForm(data, files)

            if form.is_valid():
                Product.objects.create(
                    categories=form.cleaned_data.get('categories'),
                    title=form.cleaned_data.get('title'),
                    image=form.cleaned_data.get('image'),
                    description=form.cleaned_data.get('description'),
                    price=form.cleaned_data.get('price'),
                    discount=form.cleaned_data.get('discount'),
                    quantity=form.cleaned_data.get('quantity'),
                    size=form.cleaned_data.get('size'),
                    weight=form.cleaned_data.get('weight'),
                    rate=form.cleaned_data.get('rate'),
                )
                return redirect('/products/')

            return render(request, 'products/create.html', context={
                'form': form
            })

    return redirect('/users/login')


def category_create_view(request):
    if request.user.is_authenticated:

        if request.method == 'GET':

            context_data = {
                'form': CategoryCreateForm
            }

            return render(request, 'products/categories.html', context=context_data)

        if request.method == 'POST':
            data = request.POST
            form = CategoryCreateForm(data)

            if form.is_valid():
                Category.objects.create(
                    title=form.cleaned_data.get('title'),
                )
                return redirect('/categories/')

            return render(request, 'products/categories.html', context={
                'form': form
            })

    return redirect('/users/login')
