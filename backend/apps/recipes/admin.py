from django.contrib import admin

from ..ingredients.choices import MeasurementUnit
from .models import (
    Recipe,
    RecipeIngredient,
)


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient
    readonly_fields = ['unit_exists']
    fields = ['ingredient', 'amount', 'unit', 'unit_exists']

    @admin.display(description='Unit weight?', boolean=True)
    def unit_exists(self, obj):
        if obj.unit == MeasurementUnit.GRAM:
            return True
        return obj.ingredient.measurement.filter(unit=obj.unit).exists()


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'fat', 'carbs']
    filter_horizontal = ['ingredients']
    inlines = [RecipeIngredientAdmin]
