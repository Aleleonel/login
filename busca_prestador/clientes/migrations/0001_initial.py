# Generated by Django 3.1.3 on 2020-11-15 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('endereco', '0001_initial'),
        ('veiculos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('nasc', models.DateField(blank=True, null=True)),
                ('tel01', models.CharField(max_length=11)),
                ('tel02', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('contato', models.CharField(max_length=50, unique=True)),
                ('vtipo', models.CharField(choices=[('LEVE', 'LEVE'), ('PESADO', 'PESADO')], max_length=6)),
                ('cadastro', models.DateField(auto_now=True, null=True)),
                ('endereco', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='endereco.endereco')),
                ('veiculo', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='veiculos.veiculos')),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
    ]
