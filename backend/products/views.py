from rest_framework import generics,permissions, authentication
# Create your views here.

from api.mixins import StaffEditorPermissionMixin 
from .models import Product
from .serializers import ProductSerializers


class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    authentication_classes = [authentication.SessionAuthentication, 
                              authentication.TokenAuthentication]
   

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailAPIView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    #lookup_field = "pk"

product_detail_view = ProductDetailAPIView.as_view()

class ProductUpdateAPIView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"

product_update_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = "pk"

product_delete_view = ProductDeleteAPIView.as_view()

