from django.shortcuts import render
from .models import MenuItem


# Create your views here.


def menu(request):
    
    menu_starters = MenuItem.objects.filter(category="starter")
    
    return render(
        request,
        "menu/menu.html",
        {
            "menu": "menu",
            "menu_starters": menu_starters
        }
        )
