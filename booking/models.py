from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator #https://www.geeksforgeeks.org/limit-the-maximum-value-of-a-numeric-field-in-a-django-model/

TIMES = (
    (12, '12:00 - 13:00'),
    (13, '13:00 - 14:00'),
    (14, '14:00 - 15:00'),
    (15, '15:00 - 16:00'),
    (16, '16:00 - 17:00'),
    (17, '17:00 - 18:00'),
    (18, '18:00 - 19:00'),
    (19, '19:00 - 20:00'),
    (20, '20:00 - 21:00'),
    (21, '21:00 - 22:00'),
    (22, '22:00 - 23:00'),
)

class Allergen(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Stores a single booking request.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user"
    )
    date = models.DateField(blank=True)
    time_slot = models.IntegerField(choices=TIMES)
    guests = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    allergies = models.ManyToManyField(Allergen, blank=True)
    booking_notes = models.TextField()

    class Meta:
        ordering = ["-date"]

    @property
    def name(self):
        return self.user.first_name

    def __str__(self):
        return f"Booking for {self.name} on {self.date}"
        
    