# Generated by Django 4.2.3 on 2023-07-21 01:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogsite", "0003_alter_post_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="slug",
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
