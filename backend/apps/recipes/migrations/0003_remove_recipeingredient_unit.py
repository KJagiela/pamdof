# Generated by Django 4.2.5 on 2023-10-04 20:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_recipe_original_url"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipeingredient",
            name="unit",
        ),
    ]