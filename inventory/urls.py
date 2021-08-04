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


]