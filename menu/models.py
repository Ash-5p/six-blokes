from django.db import models
from cloudinary.models import CloudinaryField
from booking.models import Allergen

CATEGORY = (
    ('starter', 'Starters'),
    ('burger', 'Burgers'),
    ('side', 'Sides'),
    ('dessert', 'Desserts'),
    ('drink', 'Drinks'),
)


class MenuItem(models.Model):
    """
    Stores a single menu item.
    """
    name = models.CharField(max_length=200)
    category = models.CharField(choices=CATEGORY)
    allergens = models.ManyToManyField(Allergen, blank=True)
    description = models.TextField()
    item_image = CloudinaryField('image', default='placeholder')
