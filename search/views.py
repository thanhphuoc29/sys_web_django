from django.shortcuts import render,redirect
from product.models import Product, Book
from catalog.models import Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from imagehash import average_hash
from PIL import Image
# Create your views here.
import json
from django.core.files.storage import FileSystemStorage

from product.forms import ImageUploadForm
from search.utils import *

# Create your views here.
def search_product_by_key(request):
    query = request.GET.get('search','')
    categories = Category.objects.all()
    # Chuẩn bị dữ liệu cho mỗi danh mục
    category_items = []
    for category in categories:
        items = filter(query,category.id)
        category_items.append({
            'category': category,
            'items': items
        })
    context = {'category_items': category_items}
    return render(request,'home_product.html', context)

def vocie_search(request):
    query = request.GET.get('search','')
    categories = Category.objects.all()
    # Chuẩn bị dữ liệu cho mỗi danh mục
    category_items = []
    for category in categories:
        items = filter(query,category.id)
        category_dict = {
            'id':category.id,
            'name':category.name,
            'type_product':category.type_product
        }
        items_list = toDict(items)
        category_items.append({
            'category': category_dict,
            'items': items_list
        })
    return JsonResponse(category_items, safe=False)

def search_product_by_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(image.name, image)
            uploaded_image_path = fs.path(filename)
            
            # Mở và tính hash cho hình ảnh được tải lên
            uploaded_image = Image.open(uploaded_image_path)
            uploaded_hash = average_hash(uploaded_image)
            
            # So sánh với các hình ảnh sản phẩm trong cơ sở dữ liệu
            similar_products = []
            products = getAllProducts()
            for product in products:
                product_image_path = product.image.path
                product_image = Image.open(product_image_path)
                product_hash = average_hash(product_image)
                
                # So sánh hash; bạn có thể điều chỉnh ngưỡng
                if abs(uploaded_hash - product_hash) < 3:  # Ngưỡng này có thể điều chỉnh
                    similar_products.append(product)
            
            categories = Category.objects.all()
            category_items = []
            for category in categories:
                print(category.id)
                items = filterByCategory(similar_products,category.id)
                category_items.append({
                    'category': category,
                    'items': items
                })
            # Xóa file tạm sau khi xử lý
            fs.delete(filename)
        
            return render(request, 'home_product.html', {'category_items': category_items})
    else:
        form = ImageUploadForm()
    return render(request, 'home_product.html', {'form': form})







