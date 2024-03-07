from django.contrib import admin
from .models import Product
from catalog.models import Category
from django import forms
# Register your models here.

admin.site.register(Product)