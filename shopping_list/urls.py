from rest_framework import routers
from django.urls import path, include
from shopping_list.api.viewsets import ShoppingItemViewSet

router = routers.DefaultRouter()
router.register("shopping-items", ShoppingItemViewSet, basename="shopping-items")

urlpatterns = [
    path("api/", include(router.urls))
]