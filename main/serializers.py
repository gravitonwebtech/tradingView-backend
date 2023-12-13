from rest_framework import serializers
from .models import MainContact

class ContactSerilizers(serializers.ModelSerializer):
    class Meta:
        model=MainContact
        fields='__all__'