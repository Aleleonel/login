# Generated by Django 3.1.2 on 2020-11-24 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instalacao', '0002_auto_20201124_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='instalacao',
            name='instalado',
            field=models.CharField(choices=[('NÃO', 'NÃO'), ('SIM', 'SIM'), ('PENDENTE', 'PENDENTE')], default='NÃO', max_length=8, null=True, verbose_name='instalado'),
        ),
    ]
