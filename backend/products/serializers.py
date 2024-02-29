from rest_framework import serializers
from .models import Product


class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "pk",
            "title",
            "content",
            "price",
            "sale_price",
            "get_discount"
        ]