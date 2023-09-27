from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.get_all_customers, name='customers'),
    path('products.html/', views.get_all_products, name='products.html'),
    # path('orders/', views.get_all_orders, name='orders'),
]