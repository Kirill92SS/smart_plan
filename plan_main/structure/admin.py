from django.contrib import admin
from .models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    pass
