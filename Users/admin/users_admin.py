from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from ..models.info_model import InfoPersonal
from ..models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ("email","is_staff","is_superuser")
    ordering = "email"
    search_fields = "email"

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Permisos", {"fields": ("is_active","is_staff","is_superuser","groups","user_permissions")}),
    )
    add_fieldsets = (
        (None, {"classes": ("wide",), "fields": ("email", "password1", "password2","is_staff", "is_superuser", "groups", "user_permissions")}),

    )


admin.site.register(CustomUser,CustomUserAdmin)
