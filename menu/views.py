from django.shortcuts import render
from .models import MenuItem


def menu(request):
    """
    Display categorised list of all instances of :model:`menu.MenuItem`.

    **Context**

    ``menu_starters``
        All instances of :model:`menu.MenuItem` where catergory="starter".
    ``menu_burgers``
        All instances of :model:`menu.MenuItem` where catergory="burger".
    ``menu_sides``
        All instances of :model:`menu.MenuItem` where catergory="side".
    ``menu_desserts``
        All instances of :model:`menu.MenuItem` where catergory="dessert".
    ``menu_drinks``
        All instances of :model:`menu.MenuItem` where catergory="drink".

    **Template:**

    :template:`menu/menu.html`
    """
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
