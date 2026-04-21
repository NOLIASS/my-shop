from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from django.contrib import messages
from .models import Category, Product, CartItem, ProductRating
from .forms import NewsletterForm, RatingForm


def get_base_context():
    return {'categories': Category.objects.all()}


def home(request):
    # Форма розсилки
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Ви успішно підписались на розсилку!")
            return redirect('home')
        else:
            messages.error(request, "❌ Цей email вже зареєстрований.")
    else:
        form = NewsletterForm()

    context = {
        **get_base_context(),
        'title':           'Головна',
        'products':        Product.objects.filter(in_stock=True),
        'newsletter_form': form,
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

    if not request.session.session_key:
        request.session.create()
    session = request.session.session_key

    avg_rating = ProductRating.objects.filter(
        product=product
    ).aggregate(Avg('score'))['score__avg']

    user_rated = ProductRating.objects.filter(
        product=product, session_key=session
    ).exists()

    if request.method == 'POST' and 'score' in request.POST:
        form = RatingForm(request.POST)
        if form.is_valid() and not user_rated:
            ProductRating.objects.create(
                product=product,
                session_key=session,
                score=int(form.cleaned_data['score'])
            )
            messages.success(request, "✅ Дякуємо за вашу оцінку!")
            return redirect('product', slug=slug)
    else:
        form = RatingForm()

    context = {
        **get_base_context(),
        'product':     product,
        'avg_rating':  round(avg_rating, 1) if avg_rating else None,
        'user_rated':  user_rated,
        'rating_form': form,
    }
    return render(request, 'shop/product_detail.html', context)


def cart(request):
    if not request.session.session_key:
        request.session.create()
    session = request.session.session_key
    items   = CartItem.objects.filter(session_key=session).select_related('product')
    total   = sum(i.total_price() for i in items)
    context = {
        **get_base_context(),
        'title': 'Кошик',
        'items': items,
        'total': total,
    }
    return render(request, 'shop/cart.html', context)


def add_to_cart(request, slug):
    if not request.session.session_key:
        request.session.create()
    product = get_object_or_404(Product, slug=slug)
    item, created = CartItem.objects.get_or_create(
        session_key=request.session.session_key,
        product=product,
        defaults={'quantity': 1}
    )
    if not created:
        item.quantity += 1
        item.save()
    messages.success(request, f"✅ '{product.name}' додано в кошик!")
    return redirect('cart')


def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart')


def about(request):
    context = {**get_base_context(), 'title': 'Про нас'}
    return render(request, 'shop/about.html', context)


def contacts(request):
    context = {**get_base_context(), 'title': 'Контакти'}
    return render(request, 'shop/contacts.html', context)