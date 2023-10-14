from django.urls import path
from rest_framework import routers

from apps.ingredients.api.views import (
    IgredientsViewSet,
    ListUnitsView,
)

app_name = 'ingredients'

router = routers.DefaultRouter()
router.register('', IgredientsViewSet, basename='ingredient')

urlpatterns = [
    path('units/', ListUnitsView.as_view(), name='units'),
] + router.urls
