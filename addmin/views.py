
from addmin.serializers import *
from rest_framework import viewsets
 
class StockFundsViewSet(viewsets.ModelViewSet):
    queryset=StockFunds.objects.all()
    serializer_class=StockFundsSerializers



class AmountAccountViewSet(viewsets.ModelViewSet):
    queryset=AmountAccount.objects.all()
    serializer_class=AmountAccountSerializers


class Stock_formViewSet(viewsets.ModelViewSet):
    queryset=Stock_form.objects.all()
    serializer_class=Stock_formSerializers