# myapp/models.py
from django.db import models

class Party(models.Model):
    PARTY_ID = models.CharField(max_length=40, primary_key=True)
    PARTY_TYPE_ENUM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)

class Person(models.Model):
    PARTY_ID = models.OneToOneField(Party, on_delete=models.CASCADE, primary_key=True)
    SALUTATION = models.CharField(max_length=255, default=None, null=True, blank=True)
    FIRST_NAME = models.CharField(max_length=255, default=None, null=True, blank=True)
    MIDDLE_NAME = models.CharField(max_length=255, default=None, null=True, blank=True)
    LAST_NAME = models.CharField(max_length=255, default=None, null=True, blank=True)
    GENDER = models.CharField(max_length=1, default=None, null=True, blank=True)
    BIRTH_DATE = models.DateField(default=None, null=True, blank=True)
    MARITAL_STATUS_ENUM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    EMPLOYMENT_STATUS_ENUM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    OCCUPATION = models.CharField(max_length=255, default=None, null=True, blank=True)

class Product(models.Model):
    PRODUCT_ID = models.CharField(max_length=40, primary_key=True)
    OWNER_PARTY_ID = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True, blank=True)
    PRODUCT_NAME = models.CharField(max_length=255, default=None, null=True, blank=True)
    DESCRIPTION = models.CharField(max_length=4095, default=None, null=True, blank=True)
    CHARGE_SHIPPING = models.CharField(max_length=1, default=None, null=True, blank=True)
    RETURNABLE = models.CharField(max_length=1, default=None, null=True, blank=True)

class OrderHeader(models.Model):
    ORDER_ID = models.CharField(max_length=40, primary_key=True)
    ORDER_NAME = models.CharField(max_length=255, default=None, null=True, blank=True)
    PLACED_DATE = models.DateTimeField(default=None, null=True, blank=True)
    APPROVED_DATE = models.DateTimeField(default=None, null=True, blank=True)
    STATUS_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    CURRENCY_UOM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    PRODUCT_STORE_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    SALES_CHANNEL_ENUM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    GRAND_TOTAL = models.DecimalField(max_digits=24, decimal_places=4, default=None, null=True, blank=True)
    COMPLETED_DATE = models.DateTimeField(default=None, null=True, blank=True)

class OrderPart(models.Model):
    ORDER_ID = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    ORDER_PART_SEQ_ID = models.CharField(max_length=40)
    PART_NAME = models.CharField(max_length=255, default=None, null=True, blank=True)
    STATUS_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    VENDOR_PARTY_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    CUSTOMER_PARTY_ID = models.ForeignKey(Party, on_delete=models.SET_NULL, null=True, blank=True)
    PART_TOTAL = models.DecimalField(max_digits=24, decimal_places=4, default=None, null=True, blank=True)
    FACILITY_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    SHIPMENT_METHOD_ENUM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)

class OrderItem(models.Model):
    ORDER_ID = models.ForeignKey(OrderHeader, on_delete=models.CASCADE)
    ORDER_ITEM_SEQ_ID = models.CharField(max_length=40)
    ORDER_PART_SEQ_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    PRODUCT_ID = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    ITEM_DESCRIPTION = models.CharField(max_length=255, default=None, null=True, blank=True)
    QUANTITY = models.DecimalField(max_digits=26, decimal_places=6, default=None, null=True, blank=True)
    UNIT_AMOUNT = models.DecimalField(max_digits=25, decimal_places=5, default=None, null=True, blank=True)
    ITEM_TYPE_ENUM_ID = models.CharField(max_length=40, default=None, null=True, blank=True)
    PARENT_ITEM_SEQ_ID = models.CharField(max_length=40, default=None, null=True, blank=True)

