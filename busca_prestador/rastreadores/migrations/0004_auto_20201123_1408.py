# Generated by Django 3.1.2 on 2020-11-23 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastreadores', '0003_auto_20201119_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rastreador',
            name='instalado',
            field=models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], default='SIM', max_length=3, null=True),
        ),
    ]