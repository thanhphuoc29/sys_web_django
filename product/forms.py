# forms.py

from django import forms
from .models import Product,Book
import random

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image','category_id']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'description', 'price', 'image','category_id','author']


class ImageUploadForm(forms.Form):
    image = forms.ImageField()

        
