# Generated by Django 4.2.5 on 2023-10-14 17:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ingredients", "0008_remove_fodmapinfo_fodmap_level_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="fodmapinfo",
            name="green_serving_size",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="fodmapinfo",
            name="red_serving_size",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="fodmapinfo",
            name="yellow_serving_size",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
