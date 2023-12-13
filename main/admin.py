from django.contrib import admin
from .models import MainContact
# Register your models here.

class MainAdmin(admin.ModelAdmin):
    pass

admin.site.register(MainContact)