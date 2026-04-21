from django.shortcuts import render
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
        'title':      'Всі категорії',
        'categories_list': Category.objects.all(),
    }
    return render(request, 'shop/categories.html', context)


def about(request):
    context = {**get_base_context(), 'title': 'Про нас'}
    return render(request, 'shop/about.html', context)


def contacts(request):
    context = {**get_base_context(), 'title': 'Контакти'}
    return render(request, 'shop/contacts.html', context)