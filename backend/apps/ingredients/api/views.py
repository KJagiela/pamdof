from rest_framework import (
    views,
    viewsets,
)
from rest_framework.response import Response

from apps.ingredients.api.seializers import IngredientSerializer
from apps.ingredients.choices import MeasurementUnit
from apps.ingredients.models import Ingredient


class ListUnitsView(views.APIView):
    def get(self, request, *args, **kwargs):
        return Response([mu.value for mu in MeasurementUnit])


class IgredientsViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
