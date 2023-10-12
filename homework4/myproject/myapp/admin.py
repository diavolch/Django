from django.contrib import admin

# Register your models here.
from .models import Customer, Product, Order


@admin.action(description='Обнулить количество товара')
def reset_quant(modeladmin, request, queryset):
    queryset.update(count=0)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address', 'date_of_registered']
    fieldsets = [
        ('Общие параметры',
         {'classes': ['wide'],
          'description': 'Общая информация',
          'fields': ['name', 'email']}),
    ]
    search_fields = ['name', 'address']
    list_per_page = 10


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'price', 'count', 'img']
    ordering = ['price']
    fieldsets = [
        ('Общие параметры',
         {'classes': ['wide'],
          'description': 'тут общие параметры',
          'fields': ['title', 'price']}),
    ]
    search_fields = ['title']
    list_filter = ['count']
    list_per_page = 10


class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'product', 'total_price', 'date_ordered']
    ordering = ['total_price']
    # fieldsets = [
    #     ('Общие параметры',
    #      {'classes': ['wide'],
    #       'description': 'Общая информация',
    #       'fields': ['title', 'price']}),
    # ]
    search_fields = ['customer', 'product']
    list_per_page = 10


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
