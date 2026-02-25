from django.contrib import admin
from ..models.users_models import CustomUser
from ..models.info_model import InfoPersonal

class InfoPersonalAdmin(admin.ModelAdmin):
    model = InfoPersonal
    can_delete = False
    verbose_name_plural = "Info personal"
    verbose_name = "Datos personales"

class InfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'telefono', 'pais', 'edad')
    search_fields = ("telefono",)
    list_filter = ("pais",)

    list_per_page = 35

    fieldsets = (
        ("Información personal", {
            "classes": ("wide",),
            "fields": ("telefono","pais", "edad")
        }),
    )

    @admin.display(description="Usuario")
    def user(self, obj):
        return CustomUser.objects.get(personal_info=obj).email



admin.site.register(InfoPersonal,InfoPersonalAdmin)