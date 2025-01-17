from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .models import Booking, Allergen

# Create your views here.
def index(request):
    return HttpResponse("Test")