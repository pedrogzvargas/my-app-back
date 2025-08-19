from rest_framework.viewsets import ModelViewSet
from products.models import Product
from .product_serializer import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.order_by('-id').all()
    serializer_class = ProductSerializer
