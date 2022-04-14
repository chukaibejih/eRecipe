from django.contrib import admin
from services.models import Recipe, Category, Occasion

# Register your models here.
admin.site.register(Recipe)
admin.site.register(Category)
admin.site.register(Occasion)
