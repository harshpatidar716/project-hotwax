
# serializers.py

from  rest_framework  import serializers
from .models import Person, Product, OrderHeader, OrderPart, OrderItem

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class OrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderHeader
        fields = '__all__'

class OrderPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderPart
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
