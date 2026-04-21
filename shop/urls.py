from django.urls import path
from . import views

urlpatterns = [
    path('',                            views.home,             name='home'),
    path('categories/',                 views.categories,       name='categories'),
    path('category/<slug:slug>/',       views.category_detail,  name='category'),
    path('product/<slug:slug>/',        views.product_detail,   name='product'),
    path('cart/',                       views.cart,             name='cart'),
    path('cart/add/<slug:slug>/',       views.add_to_cart,      name='add_to_cart'),
    path('cart/remove/<int:item_id>/',  views.remove_from_cart, name='remove_from_cart'),
    path('about/',                      views.about,            name='about'),
    path('contacts/',                   views.contacts,         name='contacts'),
]