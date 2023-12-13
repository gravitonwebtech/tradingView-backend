from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path , include
from .views import ContactViewSet

router=DefaultRouter()
router.register('main_contact',ContactViewSet)

urlpatterns = [
    path('',include(router.urls))
]