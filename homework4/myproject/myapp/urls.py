from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('customers/', views.get_all_customers, name='customers'),
    path('products/', views.get_all_products, name='products'),
    # path('get_orders/<int:customer_id>/<int:days>/', views.get_orders, name='get_orders'),
    # path('create_customer/', views.create_customer, name='create_customer'),
    # path('create_product/', views.create_product, name='create_product'),

]