# Generated by Django 4.2.3 on 2023-07-24 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("relaciones", "0002_tipocombustible_modeloauto_tipo_combustible"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="tipocombustible",
            options={
                "ordering": ["-created"],
                "verbose_name": "combustible",
                "verbose_name_plural": "combustibles",
            },
        ),
        migrations.CreateModel(
            name="DirectorEjecutivo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "nombre",
                    models.CharField(
                        blank=True, max_length=255, verbose_name="Director Ejecutivo"
                    ),
                ),
                (
                    "created",
                    models.DateField(
                        auto_now_add=True, verbose_name="Fecha de Creación"
                    ),
                ),
                (
                    "updated",
                    models.DateField(
                        auto_now=True, verbose_name="Fecha de Actualización"
                    ),
                ),
                (
                    "marca",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="relaciones.marca",
                        verbose_name="Marca",
                    ),
                ),
            ],
            options={
                "verbose_name": "director ejecutivo",
                "verbose_name_plural": "directores ejecutivod",
                "ordering": ["-created"],
            },
        ),
    ]
