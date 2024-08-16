from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class ContractManufacturerAPIView(generics.RetrieveAPIView):
    """Представление для выдачи айдишников производителей по номеру контракта"""
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer

    def get(self, request, *args, **kwargs):
        contract_id = kwargs.get('contract_id')
        contract = get_object_or_404(Contract, contract_id=contract_id)
        serializer = self.get_serializer(contract)
        return Response(serializer.data, status=status.HTTP_200_OK)


# Представления для создания записей
class ManufacturerCreateAPIView(generics.CreateAPIView):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class ContractCreateAPIView(generics.CreateAPIView):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer


class CreditApplicationCreateAPIView(generics.CreateAPIView):
    queryset = CreditApplication.objects.all()
    serializer_class = CreditApplicationSerializer


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
