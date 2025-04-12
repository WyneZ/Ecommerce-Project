from django.db import models

from backend.categories.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.URLField(blank=True)
    category = models.CharField(200, null=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=200)

    def __str__(self):
        return self.title