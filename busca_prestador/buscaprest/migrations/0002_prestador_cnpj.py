# Generated by Django 3.1.2 on 2020-11-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buscaprest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestador',
            name='cnpj',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
