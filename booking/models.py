from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MaxValueValidator #https://www.geeksforgeeks.org/limit-the-maximum-value-of-a-numeric-field-in-a-django-model/

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
    name = models.CharField(max_length=200, default="")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="booking_user", blank=True
    )
    date = models.DateField()
    timeSlot = models.IntegerField(choices=TIMES)
    guests = models.PositiveIntegerField(validators=[MaxValueValidator(12)])
    # allergies = models.ManyToManyField(Allergen, blank=True)
    bookingNotes = models.TextField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"Booking by {self.name} on {self.date}"
        
    