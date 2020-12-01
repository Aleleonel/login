import os
import uuid

from django.db import models
from django.urls import reverse_lazy
from instalacao.models import Instalacao


# customização do nome do arquivo
def get_file_path(instance, filename):
    ext = filename.split("."[-1])
    filename = "%s.%s" % (uuid.uuid4(), ext)

    return os.path.join("photos_vistoria", filename)


class Imagens(models.Model):
    titulo = models.CharField(max_length=100, null=True, blank=True)
    fotos = models.FileField(upload_to=get_file_path, null=True, blank=True)
    instalacao = models.ForeignKey(Instalacao, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse_lazy('image:imagens_detail', kwargs={'pk': self.pk})