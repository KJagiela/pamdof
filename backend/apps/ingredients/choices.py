from django.db import models


class FODMAP(models.IntegerChoices):
    FRUCTOSE = 1
    LACTOSE = 2
    MANNITOL = 3
    SORBITOL = 4
    GOS = 5
    FRUCTANS = 6


class FODMAPLevel(models.IntegerChoices):
    HIGH = 1
    MODERATE = 2
    SAFE = 3
