# Generated by Django 4.2.5 on 2023-10-14 17:10

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("ingredients", "0009_alter_fodmapinfo_green_serving_size_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="fodmapinfo",
            name="fodmap",
        ),
        migrations.AddField(
            model_name="fodmapinfo",
            name="fodmaps",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.IntegerField(
                    choices=[
                        (1, "Fructose"),
                        (2, "Lactose"),
                        (3, "Mannitol"),
                        (4, "Sorbitol"),
                        (5, "Gos"),
                        (6, "Fructans"),
                    ]
                ),
                default=[],
                size=None,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="fodmapinfo",
            name="ingredient",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="ingredients.ingredient"
            ),
        ),
    ]
