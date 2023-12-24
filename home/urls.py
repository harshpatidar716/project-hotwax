
from django.contrib import admin
from django.urls import path,include
from home import views

from django.conf import settings
from django.conf.urls.static import static


# urls.py

from django.urls import path
from .views import (
    PersonListCreateView,
    ProductListCreateView,
    OrderHeaderListCreateView,
    OrderPartListCreateView,
    OrderItemListCreateView,
)

urlpatterns = [
    path('persons/', PersonListCreateView.as_view(), name='person-list-create'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('orders/', OrderHeaderListCreateView.as_view(), name='order-header-list-create'),
    path('order-parts/', OrderPartListCreateView.as_view(), name='order-part-list-create'),
    path('order-items/', OrderItemListCreateView.as_view(), name='order-item-list-create'),
    # Add other URLs for retrieval, update, and delete operations
]

