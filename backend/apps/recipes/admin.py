from django.contrib import admin

from .models import (
    Recipe,
    RecipeIngredient,
)


class RecipeIngredientAdmin(admin.TabularInline):
    list_display = ['recipe', 'ingredient', 'amount', 'unit']
    model = RecipeIngredient


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['name', 'calories', 'protein', 'fat', 'carbs']
    filter_horizontal = ['ingredients']
    inlines = [RecipeIngredientAdmin]
