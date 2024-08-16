from rest_framework import serializers
from .models import *


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name']
        read_only_fields = ['id', 'created_at']


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ['id', 'contract_id']
        read_only_fields = ['id', 'created_at']


class CreditApplicationSerializer(serializers.ModelSerializer):
    manufacturers_id = serializers.SerializerMethodField()

    class Meta:
        model = CreditApplication
        fields = ['id', 'contract', 'manufacturers_id']
        read_only_fields = ['id', 'created_at']

    def get_manufacturers_id(self, obj):
        manufacturers_id = obj.products.values_list('manufacturer_id', flat=True).distinct()
        return manufacturers_id


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'manufacturer', 'credit_application', 'created_at']
        read_only_fields = ['id', 'created_at']
