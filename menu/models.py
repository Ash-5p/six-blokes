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

# Create your models here.
class MenuItem(models.Model):
    """
    Stores a single menu item.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user"
    )
    name = models.CharField(max_length=200, required=True)
    category = models.IntegerField(choices=CATEGORY)
    allergens = models.ManyToManyField(Allergen, blank=True)
    description = models.TextField()
