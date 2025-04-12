from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
import product_code_generator


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

    def create(self, request, *args, **kwargs):
        create_product = Product.objects.create(

        )

    serializer_class = ProductSerializer
