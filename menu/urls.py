from . import views
from django.urls import path

urlpatterns = [
    path('menu/', views.menu, name='menu')
]
