from django.db import models


# 상품 테이블
class Product(models.Model):
    store_name = models.CharField(max_length = 200)
    product_name = models.CharField(max_length = 200)
    plus = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 13, decimal_places = 2, null = True)
    url = models.CharField(max_length = 1000)
    created_at  = models.DateField(auto_now_add=True)
    
    class Meta():
        db_table = 'products'