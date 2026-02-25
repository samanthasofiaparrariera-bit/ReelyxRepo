from django.db import models

class PaisesChoices(models.TextChoices):
    SPAIN = "ES", "ESPAÑA"
    FRANCE = "FR", "FRANCIA"
    ENGLAND = "EN", "INGLATERRA"

class InfoPersonal(models.Model):
    telefono = models.CharField(max_length=11, null=True, blank=True, verbose_name="Teléfono")

    pais = models.CharField(max_length=3, choices=PaisesChoices.choices, default=PaisesChoices.SPAIN,
                            verbose_name="País", null=False, blank=False, help_text="(Obligatorio)")

    edad = models.PositiveIntegerField(default=18, choices=[(i, i) for i in range(18, 66)], verbose_name="Edad",
                                       null=False, blank=False, help_text="(Obligatorio)")

    class Meta:
        db_table = 'information_personal'
        verbose_name = '3. Dato'
        verbose_name_plural = '3. Datos'
        ordering = ['id']

    def __str__(self):
        return f"{self.telefono} ({self.pais})"
