from django.contrib import admin
from django.utils.html import format_html

from ..ingredients.choices import MeasurementUnit
from .models import (
    Recipe,
    RecipeIngredient,
)


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient
    readonly_fields = ['unit_exists', 'fodmap_level']
    fields = ['ingredient', 'amount', 'unit', 'unit_exists', 'fodmap_level']

    class Media:
        css = {'all': ('/static/css/admin-extra.css ',)}

    @admin.display(description='Unit weight?', boolean=True)
    def unit_exists(self, obj):
        if obj.unit == MeasurementUnit.GRAM:
            return True
        return obj.ingredient.measurement.filter(unit=obj.unit).exists()

    @admin.display(description='FODMAP')
    def fodmap_level(self, obj):
        color = obj.fodmap_level.value
        return format_html(
            '<span class="dot" style="background-color: {color};"></span>',
            color=color,
        )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'fat', 'carbs', 'fodmap_level']
    filter_horizontal = ['ingredients']
    inlines = [RecipeIngredientAdmin]

    class Media:
        css = {'all': ('/static/css/admin-extra.css ',)}

    @admin.display(description='FODMAP')
    def fodmap_level(self, obj):
        color = obj.fodmap_level
        return format_html(
            '<span class="dot" style="background-color: {color};"></span>',
            color=color,
        )
