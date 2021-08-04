from django.contrib import admin
from .models import Ingredient,MenuItem,RecipeRequirement

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(MenuItem)
admin.site.register(RecipeRequirement)

