from rest_framework import generics
# Create your views here.


from .models import Product
from .serializers import ProductSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_create_view = ProductCreateAPIView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers

product_detail_view = ProductDetailAPIView.as_view()