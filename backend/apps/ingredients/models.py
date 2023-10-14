from django import forms
from django.contrib.postgres.fields import ArrayField
from django.core.exceptions import ValidationError
from django.db import models

from model_utils.models import TimeStampedModel

from apps.ingredients.choices import (
    FODMAP,
    MeasurementUnit,
)


class ModifiedArrayField(ArrayField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {
            'form_class': forms.MultipleChoiceField,
            'choices': self.base_field.choices,
            'widget': forms.CheckboxSelectMultiple,
            **kwargs,
        }
        # skip ArrayField formfield implementation
        return super(ArrayField, self).formfield(**defaults)


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

    def save(self, *args, **kwargs):
        self.name = self.name.capitalize()
        super().save(*args, **kwargs)


class FODMAPInfo(TimeStampedModel):
    ingredient = models.OneToOneField(
        'ingredients.Ingredient', on_delete=models.CASCADE
    )
    fodmaps = ModifiedArrayField(
        models.CharField(choices=FODMAP.choices, max_length=16),
        default=list,
        blank=True,
    )
    green_serving_size = models.IntegerField(null=True, blank=True)
    yellow_serving_size = models.IntegerField(null=True, blank=True)
    red_serving_size = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.ingredient.name

    def clean(self):
        if self.yellow_serving_size or self.red_serving_size:
            if not self.fodmaps:
                raise ValidationError(
                    'FODMAP is required if yellow or red serving size is set.'
                )


class IngredientMeasurement(TimeStampedModel):
    ingredient = models.ForeignKey(
        'ingredients.Ingredient',
        on_delete=models.CASCADE,
        related_name='measurement',
    )
    unit = models.CharField(max_length=255, choices=MeasurementUnit.choices)
    grams = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        help_text='Grams per unit',
    )

    def __str__(self):
        return f'One {self.unit} - {self.ingredient.name} is {self.grams}g'
