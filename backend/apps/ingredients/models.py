from django.db import models

from model_utils.models import TimeStampedModel

from apps.ingredients.choices import (
    FODMAP,
    FODMAPLevel,
)


class Ingredient(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)
    calories = models.IntegerField()
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class FODMAPInfo(TimeStampedModel):
    ingredient = models.ForeignKey('ingredients.Ingredient', on_delete=models.CASCADE)
    fodmap = models.IntegerField(choices=FODMAP.choices, null=True, blank=True)
    fodmap_level = models.IntegerField(choices=FODMAPLevel.choices)
    serving_size = models.IntegerField()

    def __str__(self):
        part = ''
        if self.fodmap:
            part = f' - {self.fodmap}'
        return f'{self.ingredient.name} {part} - {self.get_fodmap_level_display()}'
