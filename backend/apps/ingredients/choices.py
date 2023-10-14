from django.db import models


class FODMAP(models.TextChoices):
    FRUCTOSE = 'fructose'
    LACTOSE = 'lactose'
    MANNITOL = 'mannitol'
    SORBITOL = 'sorbitol'
    GOS = 'gos'
    FRUCTANS = 'fructans'


class MeasurementUnit(models.TextChoices):
    GRAM = 'g'
    MILLILITER = 'ml'
    PIECE = 'pcs'
    TEASPOON = 'tsp'
    TABLESPOON = 'tbsp'
    CUP = 'cup'
