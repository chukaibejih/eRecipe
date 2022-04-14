from django.urls import path 
from services.views import RecipeViewset, CategoryViewset, OccasionViewset
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('recipes', RecipeViewset, basename='recipes')
router.register('categories', CategoryViewset, basename='categories')
router.register('occasions', OccasionViewset, basename='occasions')

urlpatterns = router.urls
