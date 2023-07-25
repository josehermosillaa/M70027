# Generated by Django 4.2.3 on 2023-07-25 00:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PrecioHistoricoVehiculos",
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
                    "fecha",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Fecha del Precio"
                    ),
                ),
                (
                    "modelo",
                    models.CharField(max_length=120, verbose_name="Modelo Auto"),
                ),
                ("precio", models.DecimalField(decimal_places=2, max_digits=10)),
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
            ],
            options={
                "verbose_name": "precio historic",
                "verbose_name_plural": "precios historicos",
                "ordering": ["-created"],
            },
        ),
    ]
