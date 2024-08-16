from django.urls import path
from .views import *

urlpatterns = [
    path('get_manufacturers_by_contract/<int:contract_id>/', ContractManufacturerAPIView.as_view(), name='get_manufacturers'),

    # Adding test data
    path('add_manufacturer/', ManufacturerCreateAPIView.as_view(), name='add_manufacturer'),
    path('add_contract/', ContractCreateAPIView.as_view(), name='add_contract'),
    #path('add_credit-application/', CreditApplicationCreateAPIView.as_view(), name='add_credit-application'),
    path('add_product/', ProductCreateAPIView.as_view(), name='add_product'),
]
