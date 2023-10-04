from django.contrib import admin

from apps.ingredients.models import (
    FODMAPInfo,
    Ingredient,
)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'fat', 'carbohydrates']


@admin.register(FODMAPInfo)
class FODMAPInfoAdmin(admin.ModelAdmin):
    pass
