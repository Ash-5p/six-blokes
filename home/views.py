from django.shortcuts import render


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
