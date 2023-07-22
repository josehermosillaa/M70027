# Generated by Django 4.2.3 on 2023-07-22 16:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("relaciones", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoCombustible",
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
                    models.CharField(max_length=255, verbose_name="Combustible"),
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
            ],
            options={
                "verbose_name": "combustible",
                "verbose_name_plural": "coombustibles",
                "ordering": ["-created"],
            },
        ),
        migrations.AddField(
            model_name="modeloauto",
            name="tipo_combustible",
            field=models.ManyToManyField(
                to="relaciones.tipocombustible", verbose_name="Combustible(s)"
            ),
        ),
    ]
