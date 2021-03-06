# Generated by Django 3.0.3 on 2020-03-29 09:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=254)),
                ('correo', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=254)),
            ],
            options={
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=254)),
                ('password', models.CharField(max_length=254)),
                ('registro_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registro.Registros')),
            ],
            options={
                'ordering': ['usuario'],
            },
        ),
    ]
