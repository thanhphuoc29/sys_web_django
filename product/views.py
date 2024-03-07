from django.shortcuts import render,redirect
from .models import Product,Category,Book
from cart.models import CartItem
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import cv2
import numpy as np
from imagehash import average_hash
from PIL import Image
# Create your views here.
import json
import random
from django.core.files.storage import FileSystemStorage

from .forms import ProductForm,ImageUploadForm,BookForm

# def product_list(request):
#     products = Product.objects.all()
#     context = {'products': products,}
#     return render(request, 'home_product.html', context)

def product_list(request):
     # Truy vấn tất cả danh mục
    categories = Category.objects.all()
    
    # Chuẩn bị dữ liệu cho mỗi danh mục
    category_items = []
    for category in categories:
        # Lấy tất cả sản phẩm trong danh mục này
        products_in_category = Product.objects.filter(category_id=category.id)
        
        # Lấy tất cả sách trong danh mục này
        books_in_category = Book.objects.filter(category_id=category.id)
        
        # Kết hợp sản phẩm và sách vào một danh sách
        items = list(products_in_category) + list(books_in_category)
        
        # Thêm vào danh sách kết quả với danh mục và các items tương ứng
        category_items.append({
            'category': category,
            'items': items
        })

    context = {'category_items': category_items}
    return render(request, 'home_product.html', context)
def get_product_list(request):
    products = Product.objects.all()
    # Tạo một list chứa dictionary của từng sản phẩm
    products_list = []
    for product in products:
        product_dict = {
            'id': product.id,
            'name': product.name,
            'description': product.description,
            'price': float(str(product.price)),
            'image': product.image.url,  # Giả sử đây là URL của ảnh
            'available': product.available,
            'created_at': product.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': product.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
            'category_id': product.category_id,
        }
        products_list.append(product_dict)
    # Trả về JSON response
    return JsonResponse(products_list, safe=False)

def product_detail(request, product_id):
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        pass  # Bỏ qua nếu không tìm thấy sản phẩm trong model Product
    if product is None:
        product = Book.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})

def Admin(request):
    phones = Product.objects.all()
    books = Book.objects.all()
    products = list(phones) + list(books)
    context = {'products': products}
    return render(request, 'admin.html', context)

def EditProduct(request,product_id):
    message = False
    product = None
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        pass  # Bỏ qua nếu không tìm thấy sản phẩm trong model Product
    if product is None:
        product = Book.objects.get(id=product_id)
        print(product.category_id)
    category = Category.objects.all()
    if request.method == 'POST':
        print('postt')
        form = ProductForm()
        pick_category = Category.objects.get(id=request.POST['category_id'])
        type_product = pick_category.type_product
        try:
            if type_product == 'Phone':
                form = ProductForm(request.POST, request.FILES, instance=product)
            elif type_product == 'Book':
                form = BookForm(request.POST, request.FILES, instance=product)
            if form.is_valid():
                form.save()
            return redirect("/manager")
        except Category.DoesNotExist:
            message = "Có lỗi xảy ra!"
    return render(request,'edit_product.html', {'product': product,'message':message,'categories':category})

def add_product(request):
    message = False
    category = Category.objects.all()
    if request.method == 'POST':
        pick_category = Category.objects.get(id=request.POST['category_id'])
        type_product = pick_category.type_product
        form = ProductForm()
        try:
            if type_product == 'Phone':
                form = ProductForm(request.POST,request.FILES)
            elif type_product == 'Book':
                form = BookForm(request.POST,request.FILES)
                print('book ne')
            if form.is_valid():
                product = form.save(commit=False)  # Lưu sản phẩm vào cơ sở dữ liệu
                product.id = random.randint(1000, 999999)
                product.save()
                print('save')
                message = "Thêm sản phẩm thành công!"
            return redirect('/manager')
        except:
            message = "Có lỗi xảy ra!"
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form,'message':message,'categories':category})

def delete_product(request,product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('/manager')

@csrf_exempt
def add_to_cart(request):
    data = {}
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        print(json_data)
        try:
            cart_item = CartItem.objects.create(
                product=json_data.get('product')['id'], # Truyền vào product_id thay vì product
                quantity=json_data.get('quantity', 1),
                status='Đợi mua hàng'
            )
            print(cart_item.status)
            cart_item.save()
            data = {
                'message': 'Thêm sản phẩm vào giỏ hàng thành công',
                'status':'OK'
            }
        except Exception as e:
            data = {
                'message': 'Có lỗi xảy ra',
                'status':'False'
            }
    return JsonResponse(data)





