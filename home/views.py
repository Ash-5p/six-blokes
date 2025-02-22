from django.shortcuts import render


# Create your views here.
def home_page(request):
    """
    Display homepage.

    **Template:**

    :template:`home/index.html`
    """
    return render(
        request,
        "home/index.html",
        {
            "home": "home",
        }
        )
