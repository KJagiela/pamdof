from django.db import models

from model_utils.models import TimeStampedModel


class Recipe(TimeStampedModel):
    name = models.CharField(max_length=255)
    original_url = models.URLField(blank=True, null=True)
    ingredients = models.ManyToManyField(
        'ingredients.Ingredient',
        through='recipes.RecipeIngredient',
    )
    instructions = models.TextField()
    servings = models.IntegerField(default=1)

    def __str__(self):
        return self.name

    def macro_sum(self, macro):
        return round(
            sum(getattr(ri, macro) for ri in self.recipeingredient_set.all())
            / self.servings,
            2,
        )

    @property
    def calories(self):
        return self.macro_sum('calories')

    @property
    def protein(self):
        return self.macro_sum('protein')

    @property
    def fat(self):
        return self.macro_sum('fat')

    @property
    def carbs(self):
        return self.macro_sum('carbs')


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
