from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_and_signup_view, name='signin_signup'),
    path('logout/', views.logout_modal_view, name="logout_modal")
]
