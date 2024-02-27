from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict
from products.serializers import ProductSerializers

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    data = request.data
    return Response(data)


