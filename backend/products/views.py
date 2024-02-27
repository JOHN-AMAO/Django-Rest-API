from rest_framework import generics
# Create your views here.


from .models import Product
from .serializers import ProductSerializers


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_detail_view = ProductDetailAPIView.as_view()