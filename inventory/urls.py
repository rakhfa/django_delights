from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('ingredients/', views.IngredientView.as_view(), name ='ingredientlist'),
    path('ingredients/add', views.CreateIngredientView.as_view(), name ='addingredient'),
    path('ingredients/<pk>/update', views.UpdateIngredientView.as_view(), name ='updateingredient'),
    path('ingredients/<pk>/delete', views.DeleteIngredientView.as_view(), name ='deleteingredient'),
    path('menuitems/', views.MenuView.as_view(), name ='menuitemlist'),
    path('menuitems/add', views.CreateMenuItemView.as_view(), name ='addmenuitem'),
    path('menuitems/<pk>/update', views.UpdateMenuItemView.as_view(), name ='updatemenuitem'),
    path('menuitems/<pk>/delete', views.DeleteMenuItemView.as_view(), name ='deletemenuitem'),
    path('recipes/', views.RecipeView.as_view(), name ='recipelist'),
    path('recipes/add', views.CreateRecipeView.as_view(), name ='addrecipe'),
    path('recipes/<pk>/update', views.UpdateRecipeView.as_view(), name ='updaterecipe'),
    path('recipes/<pk>/delete', views.DeleteRecipeView.as_view(), name ='deleterecipe'),
    path('purchase/', views.PurchaseView.as_view(), name='purchaselist'),
    path('buynow/', views.CreatePurchaseView.as_view(), name='addpurchase'),


]