from django.db import models
from django.urls import reverse_lazy


class Rastreador(models.Model):
    INSTADO_CHOICE = (
        ('SIM', 'SIM'),
        ('NÃO', 'NÃO'),

    )
    nr_rastreador = models.CharField(max_length=255)
    marca = models.CharField(max_length=25, null=True, blank=True)
    emei = models.CharField(max_length=15, null=True, blank=True)
    nr_linha = models.CharField(max_length=13, null=True, blank=True)
    provedor = models.CharField(max_length=6, null=True, blank=True)
    instalado = models.CharField(max_length=3, choices=INSTADO_CHOICE, default=INSTADO_CHOICE[0][0], null=True, blank=True)


    class Meta:
        db_table = 'rastreador'
        # ordering = ["-id"]

    def __str__(self):
        return self.nr_rastreador

    def get_absolute_url(self):
        return reverse_lazy('rastreadores:rastreadores_detail', kwargs={'pk': self.pk})
