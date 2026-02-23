from django.db import models
from django.utils.text import slugify
from rest_framework.authtoken.admin import User
from django.core.exceptions import ValidationError
from ...Users.models.users_models import CustomUser


#id, nombre, userid,conectar lista id con peli id



class Lista(models.Model):
    # FK con usuario.
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Usuario')
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    nombre = models.CharField(max_length=100, verbose_name='Nombre de la lista')
    descripcion = models.TextField(verbose_name="descripción", max_length=500, blank=True)

    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")


    class Meta:
        db_table = 'listas'
        verbose_name='Lista'
        verbose_name_plural = 'Listas'
        ordering = ['-creado']

    def __str__(self):
        return f"{self.nombre} - {self.descripcion} - {self.creado}"

    def save(self, *args, **kwargs):
        if not self.slug:
            prov = slugify(self.nombre)
            cont = 1
            while Lista.objects.filter(slug=prov).exists():
                prov = slugify(self.nombre) + "-" + str(cont)
                cont = cont + 1
            self.slug = prov

        lista = Lista.objects.filter(nombre=self.nombre).first()

        if lista is not None:
            if lista and lista.id != self.id:
                raise ValidationError({"nombre": ["Ya existe una lista con este nombre"], })
        super().save(*args, **kwargs)
