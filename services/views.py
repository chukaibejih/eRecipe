from rest_framework import viewsets, permissions
from common import permissions as custom_permissions
from services.models import Recipe, Category, Occasion
from services.serializers import RecipeSerializer, CategorySerializer, OccasionSerializer


class RecipeViewset(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_permissions(self):
        if self.action in ["update", "partial_update"]:
            return [permissions.IsAuthenticated(), custom_permissions.IsOwnerOrReadOnly()]
        return super().get_permissions()


class CategoryViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    

class OccasionViewset(viewsets.ModelViewSet):
    queryset = Occasion.objects.all()
    serializer_class = OccasionSerializer




