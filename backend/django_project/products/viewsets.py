from rest_framework import viewsets,mixins

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin,):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'