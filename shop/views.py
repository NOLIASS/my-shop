from django.shortcuts import render, get_object_or_404
from .models import Category, Product


def get_base_context():
    return {'categories': Category.objects.all()}


def home(request):
    context = {
        **get_base_context(),
        'title':    'Головна',
        'products': Product.objects.filter(in_stock=True),
    }
    return render(request, 'shop/home.html', context)


def categories(request):
    context = {
        **get_base_context(),
        'title':           'Всі категорії',
        'categories_list': Category.objects.all(),
    }
    return render(request, 'shop/categories.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category, in_stock=True)
    context = {
        **get_base_context(),
        'category': category,
        'products': products,
    }
    return render(request, 'shop/category_detail.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    context = {
        **get_base_context(),
        'product': product,
    }
    return render(request, 'shop/product_detail.html', context)


def about(request):
    context = {**get_base_context(), 'title': 'Про нас'}
    return render(request, 'shop/about.html', context)


def contacts(request):
    context = {**get_base_context(), 'title': 'Контакти'}
    return render(request, 'shop/contacts.html', context)