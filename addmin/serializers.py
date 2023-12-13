from addmin.models import *
from rest_framework import serializers


class StockFundsSerializers(serializers.ModelSerializer):
        class Meta:
          model = StockFunds
          fields="__all__"

class AmountAccountSerializers(serializers.ModelSerializer):
        class Meta:
          model = AmountAccount
          fields="__all__"


class Stock_formSerializers(serializers.ModelSerializer):
        class Meta:
          model = Stock_form
          fields="__all__"