# Generated by Django 2.1.3 on 2019-02-05 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('revista', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriadirectorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoria', models.CharField(blank=True, max_length=250, null=True)),
                ('revista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='revista_pro', to='revista.Revista')),
            ],
        ),
        migrations.CreateModel(
            name='Directorio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_publico', models.CharField(max_length=300)),
                ('palabras_clave', models.CharField(blank=True, max_length=600, null=True)),
                ('direccion', models.CharField(max_length=500)),
                ('cliente', models.CharField(max_length=200)),
                ('ubicacion', models.URLField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('telefonodos', models.CharField(blank=True, max_length=20, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('sitioweb', models.URLField(blank=True, null=True)),
                ('logotipo', models.TextField()),
                ('imagen1', models.TextField()),
                ('imagen2', models.TextField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('categori', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='catego_directorio', to='directorio.Categoriadirectorio')),
                ('revista_origen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procedencia', to='revista.Revista')),
            ],
        ),
    ]
