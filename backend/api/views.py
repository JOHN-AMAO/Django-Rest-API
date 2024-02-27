from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializers

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        data = ProductSerializers(instance).data
        #data = model_to_dict(model_data, fields=["id", "title", "content", "sale_price"])
    return Response(data)


