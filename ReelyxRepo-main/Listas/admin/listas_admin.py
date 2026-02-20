from django.contrib import admin

from Listas.models import Lista

class ListaAdmin(admin.ModelAdmin):
    list_display = ("nombre","usuario","creado")
    search_fields = ("nombre","usuario","creado")

    admin.site.register(Lista,ListaAdmin)