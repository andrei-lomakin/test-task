from rest_framework import serializers
from .models import *


class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ['name']
        read_only_fields = ['id', 'created_at']


class ContractSerializer(serializers.ModelSerializer):
    manufacturers_id = serializers.SerializerMethodField()

    class Meta:
        model = Contract
        fields = ['id', 'contract_id', 'manufacturers_id']
        read_only_fields = ['id', 'created_at']

    def get_manufacturers_id(self, obj):
        manufacturers_id = obj.credit_application.products.values_list('manufacturer_id', flat=True).distinct()
        return manufacturers_id


class CreditApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditApplication
        fields = ['id', 'contract', 'created_at']
        read_only_fields = ['id', 'created_at']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'manufacturer', 'credit_application', 'created_at']
        read_only_fields = ['id', 'created_at']
