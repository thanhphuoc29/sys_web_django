from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.cart_items, name='carts'),
    path('delete_cart_item/<int:item_id>/', views.remove_item, name='delete_cart_item'),
    path('save_item',views.save_item,name="save_item")
]