from django import forms

from django.utils import timezone
from .models import Customer, Product, Order


class CustomerForm(forms.Form):
    name = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                   'placeholder': 'Имя автора'}),
                           max_length=100)
    email = forms.EmailField(label='', initial='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'input_text long_input'}))
    phone = forms.CharField(label='', initial='Phone',
                            widget=forms.Textarea(attrs={'class': 'input_text long_input'}))
    address = forms.CharField(label='', initial='Adress',
                              widget=forms.Textarea(attrs={'class': 'input_text long_input'}))


class ProductForm(forms.Form):
    title = forms.CharField(label='', widget=forms.TextInput(attrs={'class': 'input_text long_input',
                                                                    'placeholder': 'Имя продукта'}),
                            max_length=100)
    description = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'input_text long_input',
                                                                          'placeholder': 'Описание продукта'}),
                                  max_length=100)
    price = forms.DecimalField(label='', widget=forms.NumberInput(attrs={'class': 'input_text', 'placeholder': 'Цена продукта'}))
    count = forms.IntegerField(label='', initial=0,
                               widget=forms.NumberInput(attrs={'class': 'input_text'}))
    img = forms.ImageField()


class ImageForm(forms.Form):
    image = forms.ImageField()
