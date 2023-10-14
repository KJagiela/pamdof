from django.db import models

from model_utils.models import TimeStampedModel

from apps.ingredients.choices import MeasurementUnit
from apps.ingredients.models import (
    FODMAPInfo,
    IngredientMeasurement,
)


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
        try:
            return round(
                sum(getattr(ri, macro) for ri in self.recipeingredient_set.all())
                / self.servings,
                2,
            )
        except MissingInfo as exc:
            return f'Missing measurement info: {exc.ingredient}, {exc.unit}'

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


class MissingInfo(Exception):
    def __init__(self, *args, **kwargs):
        self.ingredient = kwargs.get('ingredient')
        self.unit = kwargs.get('unit')
        super().__init__(self, *args)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('recipes.Recipe', on_delete=models.CASCADE)
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    amount = models.DecimalField(
        verbose_name='Amount',
        max_digits=8,
        decimal_places=2,
    )
    unit = models.CharField(
        max_length=255,
        choices=MeasurementUnit.choices,
        default=MeasurementUnit.GRAM,
    )

    def __str__(self):
        return f'{self.recipe.name} - {self.ingredient.name} - {self.amount}'

    @property
    def amount_g(self):
        if self.unit == MeasurementUnit.GRAM:
            return self.amount
        try:
            return self.ingredient.measurement.get(unit=self.unit).grams
        except IngredientMeasurement.DoesNotExist as exc:
            raise MissingInfo(
                ingredient=self.ingredient,
                unit=self.unit,
            ) from exc

    @property
    def calories(self):
        return self.ingredient.calories * self.amount_g / 100

    @property
    def protein(self):
        return self.ingredient.protein * self.amount_g / 100

    @property
    def fat(self):
        return self.ingredient.fat * self.amount_g / 100

    @property
    def carbs(self):
        return self.ingredient.carbs * self.amount_g / 100

    def fodmap_level(self):
        try:
            return self.ingredient.fodmapinfo
        except FODMAPInfo.DoesNotExist:
            return 'Unknown'
