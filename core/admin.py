from django.contrib import admin
from .models import EntityCatalog

@admin.register(EntityCatalog)
class EntityCatalogAdmin(admin.ModelAdmin):
    list_display = ('id_entit', 'entit_name', 'entit_active')
    search_fields = ('entit_name',)
    list_filter = ('entit_active',)
