# Generated by Django 4.2.5 on 2023-10-08 11:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0007_recipe_servings"),
    ]

    operations = [
        migrations.AddField(
            model_name="recipeingredient",
            name="unit",
            field=models.CharField(
                choices=[
                    ("g", "Gram"),
                    ("ml", "Milliliter"),
                    ("pcs", "Piece"),
                    ("tsp", "Teaspoon"),
                    ("tbsp", "Tablespoon"),
                    ("cup", "Cup"),
                ],
                default="g",
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="recipeingredient",
            name="amount",
            field=models.DecimalField(
                decimal_places=2, max_digits=5, verbose_name="Amount"
            ),
        ),
    ]