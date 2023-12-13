
from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import *

router=DefaultRouter()
router.register('stock_form',Stock_formViewSet,basename='Stock_formViewSet')
router.register('stock_fund',StockFundsViewSet,basename='StockFundsViewSet')
router.register('amount_account',AmountAccountViewSet,basename='AmountAccountViewSet')


urlpatterns = [
    path('',include(router.urls)),
    
  
]
