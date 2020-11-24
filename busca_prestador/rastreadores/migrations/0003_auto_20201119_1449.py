# Generated by Django 3.1.2 on 2020-11-19 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rastreadores', '0002_auto_20201119_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rastreador',
            name='uso',
        ),
        migrations.AddField(
            model_name='rastreador',
            name='instalado',
            field=models.CharField(blank=True, choices=[('SIM', 'SIM'), ('NÃO', 'NÃO')], max_length=3, null=True),
        ),
    ]