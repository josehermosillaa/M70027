# Generated by Django 4.2.3 on 2023-07-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("crudapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empleado",
            name="emp_designacion",
            field=models.CharField(
                choices=[
                    ("Project Manager", "Project Manager"),
                    ("Programador", "Programador"),
                    ("Soporte Técnico", "Soporte Técnico"),
                    ("Desarrollador Web", "Desarrollador Web"),
                ],
                max_length=150,
                verbose_name="Designacion",
            ),
        ),
    ]
