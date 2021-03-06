from django.db import models
from django.urls import reverse_lazy

from instaladores.models import Instaladores


class Instalacao(models.Model):

    INSTALADO_CHOICES = (
        ('NÃO', 'NÃO'),
        ('SIM', 'SIM'),
        ('PENDENTE', 'PENDENTE'),
    )
    VISTORIA_CHOICES = (
        ('NÃO', 'NÃO'),
        ('SIM', 'SIM')
    )

    placa = models.CharField('Placa', max_length=7, null=False, blank=False, unique=True)
    nome = models.CharField('Associado', max_length=30, null=False, blank=False)
    endereco = models.CharField('Endereço', max_length=60, null=False, blank=False)
    vendedor = models.CharField('Vendedor', max_length=30, null=False, blank=False, unique=True)
    instalador = models.ForeignKey(Instaladores, on_delete=models.SET_NULL, null=True, default='Não especificado')
    data_pedido = models.DateTimeField(auto_created=True)
    instalado = models.CharField(
        'instalado', max_length=8,
        null=True, choices=INSTALADO_CHOICES,
        default=INSTALADO_CHOICES[0][0]
    )
    vistoria = models.CharField(
        'Vistoria', max_length=3,
        null=True, choices=VISTORIA_CHOICES,
        default=VISTORIA_CHOICES[0][0]
    )
    obs = models.TextField(max_length=300, null=True, blank=True)

    class Meta:
        db_table = 'instalacao'
        # ordering = ["-id"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('instalacao:instalacao_detail', kwargs={'pk': self.pk})
