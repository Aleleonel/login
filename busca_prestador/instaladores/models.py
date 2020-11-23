from django.db import models
from django.urls import reverse_lazy

from endereco.models import Endereco


class Instaladores(models.Model):
    nome = models.CharField('Nome',max_length=25,)
    cpf = models.CharField('CPF', max_length=25, null=False, blank=False, unique=True)
    rg = models.CharField('R.G.', max_length=25, null=False, blank=False, unique=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.SET_NULL, null=True)
    email = models.EmailField('E-mail')
    tel01 = models.CharField('Celular', max_length=9, null=False, blank=False)
    tel02 = models.CharField('Residencial', max_length=9, null=True, blank=True)

    class Meta:
        db_table = 'instaladores'
        # ordering = ["-id"]

    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse_lazy('instaladores:instaladores_detail', kwargs={'pk': self.pk})
