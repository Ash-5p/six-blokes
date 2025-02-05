from django.shortcuts import render
from .models import MenuItem


# Create your views here.


def menu(request):
    
    menu_starters = MenuItem.objects.filter(category="starter")
    menu_burgers = MenuItem.objects.filter(category="burger")
    menu_sides = MenuItem.objects.filter(category="side")
    menu_desserts = MenuItem.objects.filter(category="dessert")
    menu_drinks = MenuItem.objects.filter(category="drink")

    context = {
        "menu_starters": menu_starters,
        "menu_burgers": menu_burgers,
        "menu_sides": menu_sides,
        "menu_desserts": menu_desserts,
        "menu_drinks": menu_drinks
    }
    
    return render(
        request,
        "menu/menu.html",
        context,
        )
