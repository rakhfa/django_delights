from django.shortcuts import render
from .models import Ingredient,MenuItem,RecipeRequirement
from django.views.generic import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import IngredientForm,MenuItemForm

def home_view(request):
    all_ingredients = Ingredient.objects.all()
    context = {"all_ingredients": all_ingredients}
    return render(request,"inventory/home.html", context)

# Create your views here.
class IngredientView(ListView):
    model = Ingredient
    template_name = "inventory/ingredients.html"

class CreateIngredientView(CreateView):
    model = Ingredient
    template_name = "inventory/add_ingredient.html"
    form_class = IngredientForm

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = "inventory/update_ingredient.html"
    form_class = IngredientForm


class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_ingredient.html"
    success_url = reverse_lazy('ingredientlist')



class MenuView(ListView):
    model = MenuItem
    template_name = "inventory/menuitems.html"

class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = "inventory/add_menuitem.html"
    form_class = MenuItemForm

class UpdateMenuItemView(UpdateView):
    model = MenuItem
    template_name = "inventory/update_menuitem.html"
    form_class = MenuItemForm


class DeleteMenuItemView(DeleteView):
    model = Ingredient
    template_name = "inventory/delete_menuitem.html"
    success_url = reverse_lazy('menuitemlist')




