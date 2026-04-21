from django.urls import path
from . import views

urlpatterns = [
    path('',                        views.home,           name='home'),
    path('categories/',             views.categories,     name='categories'),
    path('category/<slug:slug>/',   views.category_detail, name='category'),
    path('product/<slug:slug>/',    views.product_detail,  name='product'),
    path('about/',                  views.about,          name='about'),
    path('contacts/',               views.contacts,       name='contacts'),
]