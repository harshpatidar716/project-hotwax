# views.py

from rest_framework import generics
from .models import Person, Product, OrderHeader, OrderPart, OrderItem
from .serializers import PersonSerializer, ProductSerializer, OrderHeaderSerializer, OrderPartSerializer, OrderItemSerializer

class PersonListCreateView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderHeaderListCreateView(generics.ListCreateAPIView):
    queryset = OrderHeader.objects.all()
    serializer_class = OrderHeaderSerializer

class OrderPartListCreateView(generics.ListCreateAPIView):
    queryset = OrderPart.objects.all()
    serializer_class = OrderPartSerializer

class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
