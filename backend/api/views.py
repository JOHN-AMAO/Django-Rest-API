from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializers

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance)
    return Response(serializer.data)


