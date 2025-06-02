from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),
path('cart/', views.cart_detail, name='cart_detail'),
path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
path('cart/remove/<int:product_id>/', views.remove_from_cart, name='remove_from_cart'),
path('cart/increase/<int:product_id>/', views.increase_quantity, name='increase_quantity'),
path('cart/decrease/<int:product_id>/', views.decrease_quantity, name='decrease_quantity'),
path('checkout/', views.checkout, name='checkout'),
path('order-success/<int:order_id>/', views.order_success, name='order_success'),
path('category/<slug:category_slug>/', views.products_by_category, name='products_by_category'),
path('about/', views.about, name='about'),
path('contact/', views.contact, name='contact'),

]
