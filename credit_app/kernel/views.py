from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.views import APIView

from .serializers import *
from rest_framework.response import Response
from rest_framework import status


class CreditAppManufacturerAPIView(generics.RetrieveAPIView):
    """Представление для выдачи айдишников производителей по номеру контракта"""
    queryset = CreditApplication.objects.all()
    serializer_class = CreditApplicationSerializer

    def get(self, request, *args, **kwargs):
        contract_id = self.kwargs['contract_id']
        contract = Contract.objects.get(contract_id=contract_id)
        credit_application = contract.credit_application
        serializer = CreditApplicationSerializer(credit_application)
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
