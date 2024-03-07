from product.models import Product, Book
from django.core import serializers
import json

def getAllProducts():
    phones = Product.objects.all()
    books = Book.objects.all()
    products = list(phones) + list(books)
    return products


def filter(key, category_id):
    phones = Product.objects.filter(
        name__icontains=key, category_id=category_id)
    books = Book.objects.filter(name__icontains=key, category_id=category_id)
    products = list(phones) + list(books)
    return products


def filterByCategory(products, category_id):
    items = []
    for product in products:
        if int(product.category_id) == category_id:
            items.append(product)
    return items


def objectToDict(product):
    product_dict = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': float(str(product.price)),
        'image': product.image.url,
        'category_id': product.category_id,
    }
    return product_dict

def toDict(items):
    products = []
    for item in items:
        products.append(objectToDict(item))
    return products
# def toJson():
#     items_serialized = serializers.serialize('json', items)
#     items_list = json.loads(items_serialized)
