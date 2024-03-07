from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'),
    path('get_list/', views.get_product_list, name='get_products'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('manager/', views.Admin, name='admin'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.EditProduct, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('add_to_cart',views.add_to_cart,name='add_to_cart'),
    # path('search_by_key',views.search_product_by_key,name='search_by_key'),
    # path('search_by_image',views.search_product_by_image,name='search_by_image'),
    # path('search_by_voice/', views.vocie_search, name='search_by_voice'),
] 