from django.db import models
from django.conf import settings
from product.models import Product,Book
from decimal import Decimal


class CartItem(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,  # Sử dụng model User được định cấu hình trong settings của dự án
        on_delete=models.CASCADE,  # Xóa cart khi user được xóa
        related_name='carts',  # Cho phép truy cập từ User đến Cart(s)
        null=True
    )
    product = models.IntegerField(null=False)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=100,null = True,blank = True)

    def getProduct(self):
        product = None
        try:
            product = Product.objects.get(id=self.product)
        except Product.DoesNotExist:
            pass  # Bỏ qua nếu không tìm thấy sản phẩm trong model Product
        if product is None:
            product = Book.objects.get(id=self.product)
        return product
    
    def getTotalPrice(self):
        product = self.getProduct()
        return float(str(product.price)) * self.quantity
    class Meta:
        # Đặt tên bảng mới ở đây
        db_table = 'Cart_item'
