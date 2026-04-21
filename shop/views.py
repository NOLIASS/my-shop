
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Головна сторінка',
        'pages': [
            {'name': 'Категорії', 'url': 'categories'},
            {'name': 'Про нас',   'url': 'about'},
            {'name': 'Контакти',  'url': 'contacts'},
        ]
    }
    return render(request, 'shop/home.html', context)

def categories(request):
    context = {'title': 'Категорії товарів'}
    return render(request, 'shop/categories.html', context)

def about(request):
    context = {'title': 'Про нас'}
    return render(request, 'shop/about.html', context)

def contacts(request):
    context = {'title': 'Контакти'}
    return render(request, 'shop/contacts.html', context)