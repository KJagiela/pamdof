# Generated by Django 4.2.5 on 2023-10-06 16:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0006_alter_recipeingredient_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipe",
            name="servings",
            field=models.IntegerField(default=1),
        ),
    ]