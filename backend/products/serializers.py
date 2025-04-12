from rest_framework import serializers

from models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        field = ['title', 'description', 'product_price', 'image', 'category']