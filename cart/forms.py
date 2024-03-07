# forms.py

from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['user', 'product', 'quantity']
        # Bạn có thể bao gồm hoặc loại bỏ các trường tùy ý
