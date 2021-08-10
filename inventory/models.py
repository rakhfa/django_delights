from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=10)
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return "/ingredients"

    def __str__(self):
        return self.name




class MenuItem(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def get_absolute_url(self):
        return "/menuitems"

    def __str__(self):
        return self.title


class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient,on_delete=models.CASCADE)
    quantity = models.FloatField()

    def get_absolute_url(self):
        return "/recipes"

    def __str__(self):
        return self.menu_item

class Purchase(models.Model):
    menu_item=models.ForeignKey(MenuItem,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)


    def get_absolute_url(self):
        return "/purchase"







