from django.contrib import admin

from ..model.listas_model import Lista

class ListaAdmin(admin.ModelAdmin):
    list_display = ("nombre","usuario","creado")
    search_fields = ("nombre","usuario","creado")

    admin.site.register(Lista)