from django.contrib import admin
from .models import Factory


@admin.register(Factory)
class FactoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'created', 'edited', 'is_deleted']
    list_display_links = ['name']
    list_editable = ['is_deleted']
