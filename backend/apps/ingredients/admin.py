from django.contrib import admin

from apps.ingredients.models import (
    FODMAPInfo,
    Ingredient,
    IngredientMeasurement,
)


class IngredientMeasurementInline(admin.TabularInline):
    model = IngredientMeasurement
    fields = ['unit', 'grams']


class FODMAPInfoInline(admin.TabularInline):
    model = FODMAPInfo
    fields = [
        'fodmaps',
        'green_serving_size',
        'yellow_serving_size',
        'red_serving_size',
    ]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'fat', 'carbs']
    inlines = [IngredientMeasurementInline, FODMAPInfoInline]


@admin.register(FODMAPInfo)
class FODMAPInfoAdmin(admin.ModelAdmin):
    pass
