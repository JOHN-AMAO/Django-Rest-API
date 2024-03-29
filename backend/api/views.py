from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.models import Product
from django.forms.models import model_to_dict

@api_view(["GET"])
def api_home(request):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=["id", "title", "content", "sale_price"])
    return Response(data)


