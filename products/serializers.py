
from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True)

    class Meta:
        model = Product
        fields = [
            'id', 'title', 'slug', 'description',
            'category', 'category_name', 'price', 'discount_price',
            'stock', 'status', 'image', 'is_featured',
            'created_at', 'updated_at', 'is_in_stock'
        ]
        read_only_fields = ['slug', 'created_at', 'updated_at', 'is_in_stock']