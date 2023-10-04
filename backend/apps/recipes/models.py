from django.db import models

from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    name = models.CharField(max_length=255)
    original_url = models.URLField(blank=True, null=True)
    ingredients = models.ManyToManyField(
        'ingredients.Ingredient', through='recipes.RecipeIngredient'
    )
    instructions = models.TextField()

    def __str__(self):
        return self.name

    @property
    def calories(self):
        return sum(ri.calories for ri in self.recipeingredient_set.all())

    @property
    def protein(self):
        return sum(ri.protein for ri in self.recipeingredient_set.all())

    @property
    def fat(self):
        return sum(ri.fat for ri in self.recipeingredient_set.all())

    @property
    def carbs(self):
        return sum(ri.carbs for ri in self.recipeingredient_set.all())


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    amount = models.DecimalField(
        verbose_name='Amount (g)', max_digits=5, decimal_places=2
    )

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name} - {self.amount}'

    @property
    def calories(self):
        return self.ingredient.calories * self.amount / 100

    @property
    def protein(self):
        return self.ingredient.protein * self.amount / 100

    @property
    def fat(self):
        return self.ingredient.fat * self.amount / 100

    @property
    def carbs(self):
        return self.ingredient.carbs * self.amount / 100
