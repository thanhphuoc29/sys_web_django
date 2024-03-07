from catalog.models import Category
import json
from djongo import models
# Create your models here.
class Product(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null = True)
    image = models.ImageField(upload_to='images/',null = True)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.IntegerField(null = True)

    def category(self):
        return Category.objects.get(id=self.category_id)
    
    def to_json(self):
        product_data = {
            'id': self.id,
            'name': self.name,
            'price': str(self.price),  # Chuyển đổi thành chuỗi để đảm bảo định dạng JSON
            'description': self.description,
            'image': self.image.url if self.image else None  # Lấy URL của hình ảnh nếu có
            # Thêm các trường khác nếu cần
        }

        # Chuyển đổi từ điển thành chuỗi JSON
        product_json = json.dumps(product_data)
        return product_json
    

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True,null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null = True)
    image = models.ImageField(upload_to='images/',null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.IntegerField(null = True)

    def category(self):
        return Category.objects.get(id=self.category_id)
    def to_json(self):
        product_data = {
            'id': self.id,
            'name': self.name,
            'author':self.author,
            'price': str(self.price),  # Chuyển đổi thành chuỗi để đảm bảo định dạng JSON
            'description': self.description,
            'image': self.image.url if self.image else None  # Lấy URL của hình ảnh nếu có
            # Thêm các trường khác nếu cần
        }

        # Chuyển đổi từ điển thành chuỗi JSON
        product_json = json.dumps(product_data)
        return product_json

    def __str__(self):
        return self.name
