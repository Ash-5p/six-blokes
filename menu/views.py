from django.shortcuts import render


# Create your views here.
def menu(request):
    return render(
        request,
        "menu/menu.html",
        {
            "menu": "menu",
        }
        )
